import os
from stve.script import StveTestCase
from runner import TestStveTestRunner as TSTR
from nose.tools import with_setup, raises, ok_, eq_

class TestAndroidTestRuner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_01(self):
        self.base_library_execute_success("library_android_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_02(self):
        self.base_library_execute_success("library_android_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_03(self):
        StveTestCase.set("android.serial", "emulator-5554")
        self.base_library_execute_success("library_android_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_04(self):
        StveTestCase.set("android.serial", "emulator-5554")
        self.base_library_execute_success("library_android_04.py")
