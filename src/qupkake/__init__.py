"""Predict micro-pKa of organic molecules"""

# Add imports here
# from ._version import get_versions
# from .qupkake import *

# __version__ = get_versions()["version"]
__version__ = "1.0.0"

from importlib.resources import files, as_file

with as_file(files("qupkake") / "xtb/bin/xtb") as path:
    XTB_LOCATION = path.as_posix()
    # XTB_LOCATION = os.path.join(os.path.dirname(__file__), "xtb-641/bin/xtb")

XTB_VERSION = '6.4.1'