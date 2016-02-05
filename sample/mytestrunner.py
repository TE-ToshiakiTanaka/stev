import os
import sys

from stve.log import Log
from stve.application import StveTestRunner
from stve.script import StveTestCase
from stve.workspace import Workspace

def main():
    if len(sys.argv[1:]) < 1:
        sys.exit("Usage: %s <filename>" % sys.argv[0])
    testcase = sys.argv[1]

    BASE_DIR = os.path.normpath(os.path.dirname(__file__))
    SCRIPT_DIR = os.path.normpath(os.path.join(BASE_DIR, "script"))
    WORK_DIR = os.path.normpath(os.path.join(BASE_DIR, "workspace"))

    if os.path.exists(WORK_DIR):
        import shutil
        shutil.rmtree(WORK_DIR)

    workspace = Workspace(WORK_DIR)
    TMP_DIR = workspace.mkdir("tmp")
    LOG_DIR = workspace.mkdir("log")
    REPORT_DIR = workspace.mkdir("report")

    L = Log("Sample.STVE")
    StveTestCase.set("system.tmp", TMP_DIR)
    StveTestCase.set("system.log", LOG_DIR)

    runner = StveTestRunner()
    runner.execute(testcase, SCRIPT_DIR)

if __name__ == "__main__":
    main()
