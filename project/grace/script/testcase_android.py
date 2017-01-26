import os
import sys

from grace.utility import *
from grace.utility import LOG as L
from grace.script import testcase_base


class TestCase_Android(testcase_base.TestCase_Unit):

    def adb_screenshot(self, filename=None):
        if filename == None: filename = "capture.png"
        L.debug("capture file : %s" % os.path.join(TMP_DIR, filename))
        return self.adb.snapshot(filename, TMP_DIR)

    def adb_tap(self, x, y):
        return self.adb.tap(x, y)
