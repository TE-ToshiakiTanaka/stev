from runner import TestStveTestRunner as TSTR
from nose.tools import with_setup, raises, ok_, eq_

class TestPictureTestRuner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_01(self):
        self.base_library_execute_success("library_picture_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_02(self):
        self.base_library_execute_success("library_picture_02.py")
