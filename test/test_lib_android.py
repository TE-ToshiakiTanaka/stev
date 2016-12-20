import os
import sys

from stve.log import LOG as L
from stve.cmd import run
from stve.script import StveTestCase
from stve.exception import *
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
        serial = run("adb get-serialno")[1].splitlines()[-1]
        StveTestCase.set("android.serial", serial)
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_04(self):
        serial = run("adb get-serialno")[1].splitlines()[-1]
        StveTestCase.set("android.serial", serial)
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_04.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_05(self):
        serial = run("adb get-serialno")[1].splitlines()[-1]
        StveTestCase.set("android.serial", serial)
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_05.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_06(self):
        serial = run("adb get-serialno")[1].splitlines()[-1]
        StveTestCase.set("android.serial", serial)
        StveTestCase.set("system.tmp", self.data_path)
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_06.py")
