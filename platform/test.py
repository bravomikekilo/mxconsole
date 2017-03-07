# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
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

"""Testing. See the @{$python/test} guide.

@@main
@@TestCase
@@test_src_dir_path
@@assert_equal_graph_def
@@get_temp_dir
@@is_built_with_cuda
@@is_gpu_available
@@gpu_device_name
@@compute_gradient
@@compute_gradient_error
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import unittest
from mxconsole.platform import googletest as _googletest
from mxconsole.util.all_util import remove_undocumented

import sys

if sys.version_info.major == 2:
    import mock  # pylint: disable=g-import-not-at-top,unused-import
else:
    from unittest import mock  # pylint: disable=g-import-not-at-top

# Import Benchmark class
import random
import tempfile
import numpy as np

Benchmark = _googletest.Benchmark  # pylint: disable=invalid-name
DEFAULT_GRAPH_SEED = 87654321
_MAXINT32 = 2 ** 31 - 1


class TensorFlowTestCase(unittest.TestCase):
    """Base class for tests that need to test TensorFlow.
  """

    def __init__(self, methodName="runTest"):
        super(TensorFlowTestCase, self).__init__(methodName)
        self._threads = []
        self._tempdir = None

    def setUp(self):
        pass
        random.seed(DEFAULT_GRAPH_SEED)
        np.random.seed(DEFAULT_GRAPH_SEED)

    def tearDown(self):
        for thread in self._threads:
            self.assertFalse(thread.is_alive(), "A checkedThread did not terminate")

    def get_temp_dir(self):
        """Returns a unique temporary directory for the test to use.

    Across different test runs, this method will return a different folder.
    This will ensure that across different runs tests will not be able to
    pollute each others environment.

    Returns:
      string, the path to the unique temporary directory created for this test.
    """
        if not self._tempdir:
            self._tempdir = tempfile.mkdtemp(dir=_googletest.GetTempDir())
        return self._tempdir

    def assertStartsWith(self, actual, expected_start, msg=None):
        """Assert that actual.startswith(expected_start) is True.

    Args:
      actual: str
      expected_start: str
      msg: Optional message to report on failure.
    """
        if not actual.startswith(expected_start):
            fail_msg = "%r does not start with %r" % (actual, expected_start)
            fail_msg += " : %r" % (msg) if msg else ""
            self.fail(fail_msg)
    assertItemsEqual = unittest.TestCase.assertCountEqual

def main(argv=None):
    """Runs all unit tests."""
    return _googletest.main(argv)


def get_temp_dir():
    """Returns a temporary directory for use during tests.

  There is no need to delete the directory after the test.

  Returns:
    The temporary directory.
  """
    return _googletest.GetTempDir()


def test_src_dir_path(relative_path):
    """Creates an absolute test srcdir path given a relative path.

  Args:
    relative_path: a path relative to tensorflow root.
      e.g. "core/platform".

  Returns:
    An absolute path to the linked in runfiles.
  """
    return _googletest.test_src_dir_path(relative_path)

_allowed_symbols = [
   # We piggy-back googletest documentation.
    'Benchmark',
    'mock',
    'TensorFlowTestCase',
    'tempfile',
    'random',
    'DEFAULT_GRAPH_SEED',
    'np',
]

remove_undocumented(__name__, _allowed_symbols)
