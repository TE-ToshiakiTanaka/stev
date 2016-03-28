import os
from stve.script import StveTestCase
from runner import TestStveTestRunner as TSTR
from nose.tools import with_setup, raises, ok_, eq_

class TestBrowserTestRuner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_01(self):
        self.base_library_execute_success("library_browser_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_02(self):
        self.base_library_execute_success("library_browser_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_borwser_success_03(self):
        self.base_library_execute_success("library_browser_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_borwser_success_04(self):
        StveTestCase.set("browser.url", "https:\/\/www.google.co.jp")
        self.base_library_execute_success("library_browser_04.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_borwser_success_05(self):
        StveTestCase.set("browser.url", "https:\/\/www.google.co.jp")
        self.base_library_execute_success("library_browser_05.py")
