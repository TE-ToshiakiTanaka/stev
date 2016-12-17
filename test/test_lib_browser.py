import os
import sys
import platform
from stve.log import LOG as L
from stve.script import StveTestCase
from nose.tools import with_setup, raises, ok_, eq_

LIB_PATH = os.path.dirname(os.path.abspath(__file__))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from runner import TestStveTestRunner as TSTR

class TestBrowserTestRuner(TSTR):
    def get_chrome_driver_path(self):
        return self._get_driver_path("chrome")

    def get_gecko_driver_path(self):
        return self._get_driver_path("gecko")

    def _get_driver_path(self, exe):
        if platform.system() == "Linux":
            return os.path.join(
                self.bin_path, "webdriver", exe,
                    platform.system(), platform.processor(), "%sdriver" % exe)
        elif platform.system() == "Windows":
            return os.path.join(
                self.bin_path, "webdriver", exe,
                    platform.system(), "%sdriver.exe" % exe)
        else:
            return None

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_01(self):
        self.script_path = os.path.join(self.script_path, "browser")
        self.base_library_execute_success("browser_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_02(self):
        self.script_path = os.path.join(self.script_path, "browser")
        self.base_library_execute_success("browser_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_03(self):
        self.script_path = os.path.join(self.script_path, "browser")
        self.base_library_execute_success("browser_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_04_1(self):
        self.script_path = os.path.join(self.script_path, "browser")
        StveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_04_1.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_04_2(self):
        self.script_path = os.path.join(self.script_path, "browser")
        StveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_04_2.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_04_3(self):
        self.script_path = os.path.join(self.script_path, "browser")
        driver_path = self.get_chrome_driver_path()
        StveTestCase.set("browser.url", u'https://www.google.com/')
        StveTestCase.set("browser.driver", driver_path)
        self.base_library_execute_success("browser_04_3.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_04_4(self):
        self.script_path = os.path.join(self.script_path, "browser")
        StveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_04_4.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_05_1(self):
        self.script_path = os.path.join(self.script_path, "browser")
        StveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_05_1.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_05_2(self):
        self.script_path = os.path.join(self.script_path, "browser")
        driver_path = self.get_chrome_driver_path()
        StveTestCase.set("browser.url", u'https://www.google.com/')
        StveTestCase.set("browser.driver", driver_path)
        self.base_library_execute_success("browser_05_2.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_06_1(self):
        self.script_path = os.path.join(self.script_path, "browser")
        StveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_06_1.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_06_2(self):
        self.script_path = os.path.join(self.script_path, "browser")
        driver_path = self.get_chrome_driver_path()
        StveTestCase.set("browser.url", u'https://www.google.com/')
        StveTestCase.set("browser.driver", driver_path)
        self.base_library_execute_success("browser_06_2.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_07_1(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.script_path = os.path.join(self.script_path, "browser")
        StveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_07_1.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_07_2(self):
        StveTestCase.set("system.tmp", self.tmp_path)
        self.script_path = os.path.join(self.script_path, "browser")
        driver_path = self.get_chrome_driver_path()
        StveTestCase.set("browser.url", u'https://www.google.com/')
        StveTestCase.set("browser.driver", driver_path)
        self.base_library_execute_success("browser_07_2.py")
