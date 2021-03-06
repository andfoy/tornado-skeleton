# -*- coding: utf-8 -*-

"""
web module
=========

Provides:
    1. Asynchronous execution of Web Rendering and Websockets

How to use the documentation
----------------------------
Documentation is available in one form: docstrings provided
with the code

Copyright (c) 2016, Edgar A. Margffoy.
MIT, see LICENSE for more details.
"""

import os
import sys
#New submodules defined inside this module must be imported here
from . import main_handler
# from . import gpu_ws_handler
# from . import graphs_handler
from . import users_handler
from . import image_handler

__version__ = '1.0.0'

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
