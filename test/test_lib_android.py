import os
import sys
from stve.log import LOG as L
from stve.cmd import run
from stve.script import StveTestCase
from stve.exception import *
from nose.tools import with_setup, raises, ok_, eq_
try:
    import configparser
except:
    import ConfigParser as configparser

LIB_PATH = os.path.dirname(os.path.abspath(__file__))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from runner import TestStveTestRunner as TSTR

class TestAndroidTestRunner(TSTR):

    def get_serial(self):
        conf = os.path.join(self.root, "data", "config.ini")
        print(conf)
        if not os.path.exists(conf):
            serial = run("adb get-serialno")[1].splitlines()[-1]
        else:
            try:
                config = configparser.ConfigParser()
                config.read(conf)
                serial = config.get("adb", "serial")
            except Exception as e:
                print(str(e))

        return serial

    def get_apk_path(self):
        return os.path.join(
            self.bin_path, "apk", "aura")

    def get_jar_path(self):
        return os.path.join(
            self.bin_path, "jar", "aubs")

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
        serial = self.get_serial()
        StveTestCase.set("android.serial", serial)
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_04(self):
        serial = self.get_serial()
        StveTestCase.set("android.serial", serial)
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_04.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_05(self):
        serial = self.get_serial()
        StveTestCase.set("android.serial", serial)
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_05.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_06(self):
        serial = self.get_serial()
        StveTestCase.set("android.serial", serial)
        StveTestCase.set("android.apk", self.get_apk_path())
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_06.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_07(self):
        serial = self.get_serial()
        StveTestCase.set("android.serial", serial)
        StveTestCase.set("android.jar", self.get_jar_path())
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_07.py")
