# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Tensor summaries for exporting information about a model.

See the @{$python/summary} guide.

@@FileWriter
@@FileWriterCache
@@tensor_summary
@@scalar
@@histogram
@@audio
@@image
@@merge
@@merge_all
@@get_summary_description
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re as _re
import bisect as _bisect
import numpy as _np
from PIL import Image as _Image
from IO import StringIO as _StringIO
from six.moves import xrange

from google.protobuf import json_format as _json_format
# exports Summary, SummaryDescription, Event, TaggedRunMetadata, SessionLog
# pylint: disable=unused-import
from mxconsole.protobuf.summary_pb2 import Summary
from mxconsole.protobuf.summary_pb2 import SummaryDescription
from mxconsole.protobuf.event_pb2 import Event
from mxconsole.protobuf.event_pb2 import SessionLog
from mxconsole.protobuf.event_pb2 import TaggedRunMetadata
# pylint: enable=unused-import

#from mxconsole.platform import dtypes as _dtypes
from mxconsole.platform import ops as _ops
#from tensorflow.python.ops import gen_logging_ops as _gen_logging_ops
# exports tensor_summary
# pylint: disable=unused-import
#from tensorflow.python.ops.summary_ops import tensor_summary
# pylint: enable=unused-import
from mxconsole.platform import tf_logging as _logging
# exports FileWriter, FileWriterCache
# pylint: disable=unused-import
from mxconsole.summary.writer.writer import FileWriter
from mxconsole.summary.writer.writer_cache import FileWriterCache
# pylint: enable=unused-import
from mxconsole.util import compat as _compat
from mxconsole.util.all_util import remove_undocumented


def _collect(val, collections, default_collections):
  if collections is None:
    collections = default_collections
  for key in collections:
    _ops.add_to_collection(key, val)


_INVALID_TAG_CHARACTERS = _re.compile(r'[^-/\w\.]')


def _clean_tag(name):
  # In the past, the first argument to summary ops was a tag, which allowed
  # arbitrary characters. Now we are changing the first argument to be the node
  # name. This has a number of advantages (users of summary ops now can
  # take advantage of the tf name scope system) but risks breaking existing
  # usage, because a much smaller set of characters are allowed in node names.
  # This function replaces all illegal characters with _s, and logs a warning.
  # It also strips leading slashes from the name.
  if name is not None:
    new_name = _INVALID_TAG_CHARACTERS.sub('_', name)
    new_name = new_name.lstrip('/')  # Remove leading slashes
    if new_name != name:
      _logging.info(
          'Summary name %s is illegal; using %s instead.' %
          (name, new_name))
      name = new_name
  return name


def scalar(name, scalar, collections=None):
    """Outputs a `Summary` protocol buffer containing a single scalar value.
    The generated Summary has a Tensor.proto containing the input Tensor.
    Args:
      name: A name for the generated node. Will also serve as the series name in
        TensorBoard.
      tensor: A real numeric Tensor containing a single value.
      collections: Optional list of graph collections keys. The new summary op is
        added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    Returns:
      A scalar `Tensor` of type `string`. Which contains a `Summary` protobuf.
    Raises:
      ValueError: If tensor has the wrong shape or type.
    """
    name = _clean_tag(name)
    if not isinstance(scalar, float):
        # try conversion, if failed then need handle by user.
        scalar = float(scalar)
    return Summary(value=[Summary.Value(tag=name, simple_value=scalar)])


def _make_histogram_buckets():
    v = 1E-12
    buckets = []
    neg_buckets = []
    while v < 1E20:
        buckets.append(v)
        neg_buckets.append(-v)
        v *= 1.1
    # Should include DBL_MAX, but won't bother for test data.
    return neg_buckets[::-1] + [0] + buckets


def _make_histogram(values):
    """Convert values into a histogram proto using logic from histogram.cc."""
    limits = _make_histogram_buckets()
    counts = [0] * len(limits)
    for v in values:
        idx = _bisect.bisect_left(limits, v)
        counts[idx] += 1

    limit_counts = [(limits[i], counts[i]) for i in xrange(len(limits))
                    if counts[i]]
    bucket_limit = [lc[0] for lc in limit_counts]
    bucket = [lc[1] for lc in limit_counts]
    sum_sq = sum(v * v for v in values)
    return HistogramProto(min=min(values),
                          max=max(values),
                          num=len(values),
                          sum=sum(values),
                          sum_squares=sum_sq,
                          bucket_limit=bucket_limit,
                          bucket=bucket)

def histogram(name, values, collections=None):
    # pylint: disable=line-too-long
    """Outputs a `Summary` protocol buffer with a histogram.
    The generated
    [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
    has one summary value containing a histogram for `values`.
    This op reports an `InvalidArgument` error if any value is not finite.
    Args:
      name: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      values: A real numeric `Tensor`. Any shape. Values to use to
        build the histogram.
      collections: Optional list of graph collections keys. The new summary op is
        added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    Returns:
      A scalar `Tensor` of type `string`. The serialized `Summary` protocol
      buffer.
    """
    name = _clean_tag(name)
    hist = _make_histogram(values.astype(float))
    return Summary(value=[Summary.Value(tag=name, histo=hist)])

def _make_image(tensor, height, width, channel):
    """Convert an numpy representation image to Image protobuf"""
    img = _Image.fromarray(tensor)
    output = _StringIO()
    img.save(output, format='PNG')
    image_string = output.getvalue()
    output.close()
    return Summary.Image(height=height,
                         width=width,
                         colorspace=channel,
                         encoded_image_string=image_string)
                         
def image(tag, tensor):
    """Outputs a `Summary` protocol buffer with images.
    The summary has up to `max_images` summary values containing images. The
    images are built from `tensor` which must be 3-D with shape `[height, width,
    channels]` and where `channels` can be:
    *  1: `tensor` is interpreted as Grayscale.
    *  3: `tensor` is interpreted as RGB.
    *  4: `tensor` is interpreted as RGBA.
    The `name` in the outputted Summary.Value protobufs is generated based on the
    name, with a suffix depending on the max_outputs setting:
    *  If `max_outputs` is 1, the summary value tag is '*name*/image'.
    *  If `max_outputs` is greater than 1, the summary value tags are
       generated sequentially as '*name*/image/0', '*name*/image/1', etc.
    Args:
      tag: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      tensor: A 3-D `uint8` or `float32` `Tensor` of shape `[height, width,
        channels]` where `channels` is 1, 3, or 4.
    Returns:
      A scalar `Tensor` of type `string`. The serialized `Summary` protocol
      buffer.
    """
    tag = _clean_tag(tag)
    if not isinstance(tensor, _np.ndarray):
        # try conversion, if failed then need handle by user.
        tensor = _np.ndarray(tensor, dtype=np.float32)
    shape = tensor.shape
    height, width, channel = shape[0], shape[1], shape[2]
    if channel == 1:
        # walk around. PIL's setting on dimension.
        tensor = _np.reshape(tensor, (height, width))
    img = _make_image(tensor, height, width, channel)
    return Summary(value=[Summary.Value(tag=tag, image=img)])




def get_summary_description(node_def):
  """Given a TensorSummary node_def, retrieve its SummaryDescription.

  When a Summary op is instantiated, a SummaryDescription of associated
  metadata is stored in its NodeDef. This method retrieves the description.

  Args:
    node_def: the node_def_pb2.NodeDef of a TensorSummary op

  Returns:
    a summary_pb2.SummaryDescription

  Raises:
    ValueError: if the node is not a summary op.
  """

  if node_def.op != 'TensorSummary':
    raise ValueError("Can't get_summary_description on %s" % node_def.op)
  description_str = _compat.as_str_any(node_def.attr['description'].s)
  summary_description = SummaryDescription()
  _json_format.Parse(description_str, summary_description)
  return summary_description


_allowed_symbols = [
    'Summary', 'SummaryDescription', 'Event', 
    'TaggedRunMetadata', 'SessionLog', 'xrange',
]

remove_undocumented(__name__, _allowed_symbols)
