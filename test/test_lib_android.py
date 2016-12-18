import os
import sys

from stve.log import LOG as L
from stve.cmd import run
from stve.script import StveTestCase
from nose.tools import with_setup, raises, ok_, eq_

LIB_PATH = os.path.dirname(os.path.abspath(__file__))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from runner import TestStveTestRunner as TSTR

class TestAndroidTestRunner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_01(self):
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_02(self):
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_03(self):
        StveTestCase.set("android.serial", run("adb get-serialno | grep -v daemon")[1])
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_03.py")
