import os
import sys
from stve.script import StveTestCase
from nose.tools import with_setup, raises, ok_, eq_

LIB_PATH = os.path.dirname(os.path.abspath(__file__))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from runner import TestStveTestRunner as TSTR

class TestPictureTestRuner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_01(self):
        self.script_path = os.path.join(self.script_path, "picture")
        self.base_library_execute_success("picture_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_02(self):
        self.script_path = os.path.join(self.script_path, "picture")
        self.base_library_execute_success("picture_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_03(self):
        self.script_path = os.path.join(self.script_path, "picture")
        self.base_library_execute_success("picture_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_04(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_04.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_05(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_05.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_06(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_06.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_07(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_07.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_08(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_08.py")
        self.workspace.rm(os.path.join(self.data_path, "test02.png"))

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_09(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_09.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_10(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_10.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_11(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_11.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_12(self):
        self.script_path = os.path.join(self.script_path, "picture")
        StveTestCase.set("system.tmp", self.data_path)
        self.base_library_execute_success("picture_12.py")
