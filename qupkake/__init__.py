"""Predict micro-pKa of organic molecules"""

# Add imports here
from ._version import get_versions
from .qupkake import *

__version__ = get_versions()["version"]

import os

XTB_LOCATION = os.path.join(os.path.dirname(__file__), "xtb-641/bin/xtb")
XTB_VERSION = '6.4.1'