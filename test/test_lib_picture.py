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
        self.base_library_execute_success("library_picture_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_02(self):
        self.base_library_execute_success("library_picture_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_03(self):
        self.base_library_execute_success("library_picture_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_04(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_04.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_05(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_05.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_06(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_06.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_07(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_07.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_08(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_08.py")
        self.workspace.rm(os.path.join(self.tmp_path, "test02.png"))

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_09(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_09.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_10(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_10.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_11(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_11.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_12(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.base_library_execute_success("library_picture_12.py")
