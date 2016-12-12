import os
import sys
import stve

PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if not PATH in sys.path:
    sys.path.insert(0, PATH)

if stve.__version__ < "0.1.0":
    sys.exit("stve version over 0.1.0 : %s" % (stve.__version__))

from stve.application import StveTestRunner
from stve.workspace import Workspace

from stella.utility import *

class TestRunner(object):
    def __init__(self):
        self.runner = StveTestRunner()
        self.workspace = Workspace(WORK_DIR)

        self.lib = self.workspace.mkdir("lib")
        self.tmp = self.workspace.mkdir("tmp")
        self.log = self.workspace.mkdir("log")
        self.report = self.workspace.mkdir("report")
