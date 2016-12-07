import os
import sys
from stve.script import StveTestCase
from nose.tools import with_setup, raises, ok_, eq_

LIB_PATH = os.path.dirname(os.path.abspath(__file__))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from runner import TestStveTestRunner as TSTR

class TestBrowserTestRuner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_01(self):
        self.base_library_execute_success("library_browser_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_02(self):
        self.base_library_execute_success("library_browser_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_03(self):
        self.base_library_execute_success("library_browser_03.py")

    #@with_setup(TSTR.setup, TSTR.teardown)
    #def test_library_execute_browser_success_04(self):
    #    StveTestCase.set("browser.url", u'https://www.google.com/')
    #    self.base_library_execute_success("library_browser_04.py")

    #@with_setup(TSTR.setup, TSTR.teardown)
    #def test_library_execute_browser_success_05(self):
    #    StveTestCase.set("browser.url", u'https://www.google.com/')
    #    self.base_library_execute_success("library_browser_05.py")
