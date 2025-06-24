"""Predict micro-pKa of organic molecules"""

# Add imports here
from ._version import get_versions
from .qupkake import *

__version__ = get_versions()["version"]

import os
import subprocess
import shutil
import re
import tempfile

XTB_VERSION = None

try:
    XTB_LOCATION = shutil.which('xtb')
    assert XTB_LOCATION is not None
    proc = subprocess.run(['xtb', '--version'], capture_output=True, text=True)
    assert proc.returncode == 0, "xtb is not accessible"
    match = re.search('xtb\s+version\s+(?P<version>[\d.]+)', proc.stdout)
    if match:
        XTB_VERSION = match.group('version')
    assert XTB_VERSION and XTB_VERSION >= '6.4.1'

except:
    XTB_LOCATION = os.path.join(os.path.dirname(__file__), "xtb-641/bin/xtb")
    XTB_VERSION = '6.4.1'

try:
    h2o = [
        '$coord',
        ' 0.00000000000000      0.00000000000000     -0.73578586109551      o',
        ' 1.44183152868459      0.00000000000000      0.36789293054775      h',
        '-1.44183152868459      0.00000000000000      0.36789293054775      h',
        '$end',
    ]

    with tempfile.TemporaryDirectory() as temp_dir:
        test_geometry = os.path.join(temp_dir, 'coord')
        with open(test_geometry, 'w') as f:
            f.write('\n'.join(h2o))
        proc = subprocess.run(['xtb', test_geometry, '--opt'], capture_output=True, text=True)
        assert proc.returncode == 0

except:
    raise RuntimeError("""
                       
Conda installed xTB has the Fortran runtime error in geometry optimization. 
Please install xtb using the compiled binary:
                       
$ wget https://github.com/grimme-lab/xtb/releases/download/v6.7.1/xtb-6.7.1-linux-x86_64.tar.xz
$ tar -xf xtb-6.7.1-linux-x86_64.tar.xz
$ cp -r xtb-dist/bin/*      /usr/local/bin/
$ cp -r xtb-dist/lib/*      /usr/local/lib/
$ cp -r xtb-dist/include/*  /usr/local/include/
$ cp -r xtb-dist/share      /usr/local/
        
""")