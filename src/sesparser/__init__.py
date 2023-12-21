# Copyright 2023 Vaddiraju Surya Teja

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
SES Parser AWS SES Parsing library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All methods are supported - see `sesparser.api`. Full documentation
is at <https://sesparser.readthedocs.io>.

:copyright: (c) 2023 by Vaddiraju Surya Teja.
:license: Apache 2.0, see LICENSE for more details.
"""

import logging
from logging import NullHandler
from .main import (
    online,
    offline,
)
from .__version__ import(
    __title__,
    __description__,
    __url__,
    __version__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
)
logging.getLogger(__name__).addHandler(NullHandler())