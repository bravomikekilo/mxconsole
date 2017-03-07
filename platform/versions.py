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

"""TensorFlow versions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


# very dirty resolution, should be changed
# these values are extracted from a living tensorflow instance
__version__ = '1.0.0'
__git_version__ = 'v1.0.0-rc2-15-g47bba63-dirty'
__compiler_version__ = '4.8.4'

VERSION = __version__
GIT_VERSION = __git_version__
COMPILER_VERSION = __compiler_version__

GRAPH_DEF_VERSION = 21
GRAPH_DEF_VERSION_MIN_CONSUMER = 0

GRAPH_DEF_VERSION_MIN_PRODUCER = 0

__all__ = [
    "__version__",
    "__git_version__",
    "__compiler_version__",
    "COMPILER_VERSION",
    "GIT_VERSION",
    "GRAPH_DEF_VERSION",
    "GRAPH_DEF_VERSION_MIN_CONSUMER",
    "GRAPH_DEF_VERSION_MIN_PRODUCER",
    "VERSION",
]
