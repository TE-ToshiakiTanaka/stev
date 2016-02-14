from stve.script import StveTestCase
from runner import TestStveTestRunner as TSTR
from nose.tools import with_setup, raises, ok_, eq_

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
