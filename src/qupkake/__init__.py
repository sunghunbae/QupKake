from importlib.resources import files, as_file


__version__ = "1.0.0"

XTB_VERSION = '6.4.1'

with as_file(files("qupkake") / "xtb/bin/xtb") as path:
    XTB_LOCATION = path.as_posix()
