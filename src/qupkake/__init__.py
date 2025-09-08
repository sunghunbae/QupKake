from importlib.resources import files, as_file


__version__ = "1.0.0"

XTB_LOCATION = as_file(files("qupkake") / "xtb/bin/xtb").as_posix()
XTB_VERSION = '6.4.1'
