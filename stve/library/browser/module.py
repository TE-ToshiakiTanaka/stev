import sys
import os
import time
import platform

try:
    from selenium import webdriver
    from selenium.webdriver import FirefoxProfile
    from selenium.webdriver.common.action_chains import ActionChains
except Exception as e:
    print(str(e))

DRIVER_PATH = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "driver"))

from stve.log import Log
from stve.exception import *

DEFAULT_WAIT = 30
WINDOW_SIZE_WIDTH = 1280
WINDOW_SIZE_HEIGHT = 800
L = Log("Browser.Library.STVE")

class Selenium(object):
    driver = None
    mode = "FireFox"

    def __init__(self, mode="FireFox"):
        self.__mode(mode)

    @classmethod
    def __mode(cls, mode):
        cls.mode = mode

    @classmethod
    def start(cls, url, driver=""):
        try:
            if cls.mode == "FireFox":
                geckodriver = ""
                if driver != "":
                    geckodriver = driver
                    L.info(geckodriver)
                os.environ["webdriver.gecko.driver"] = geckodriver
                default_profile = {
                    'browser.usedOnWindows10': False,
                    'browser.usedOnWindows10.introURL': 'https://www.google.com/',
                    'startup.homepage_welcome_url.additional': 'about:blank',
                    'browser.startup.homepage_override.mstone': 'ignore',
                }
                profile = FirefoxProfile()
                for name, value in default_profile.items():
                    profile.set_preference(name, value)
                cls.driver = webdriver.Firefox(profile)

            elif cls.mode == "Chrome":
                try:
                    if driver != "":
                        chromedriver = driver
                        L.info(chromedriver)
                        os.environ["webdriver.chrome.driver"] = chromedriver
                        cls.driver = webdriver.Chrome(chromedriver)
                    else:
                        raise SeleniumError("Not Set Chrome Driver Path.")
                except Exception as e:
                    L.debug(str(e))
                    raise SeleniumError(
                        "Can't find Selenium Chrome Driver.")
            else:
                raise SeleniumError(
                    "Can't find Selenium Driver Mode. %s" % cls.mode)

            cls.driver.implicitly_wait(DEFAULT_WAIT)
            cls.driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
            cls.driver.get(url)
        except Exception as e:
            L.warning(str(e))
            raise SeleniumError(
                "Can't start Selenium Driver. %s" % cls.driver)

    @classmethod
    def screenshot(cls, host, filename="screen.png"):
        f = os.path.join(host, filename)
        cls.driver.save_screenshot(f)
        return f

    @classmethod
    def click(cls, element, x, y, by="class"):
        if by == "class":
            cls._click_class(element, x, y)
        elif by == "id":
            cls._click_id(element, x, y)
        elif by == "name":
            cls._click_name(element, x, y)
        else:
            raise SeleniumError(
                "Can't find Selenum Target type. %s " % element)

    @classmethod
    def find_element_by_id(cls, element):
        try:
            return cls.driver.find_element_by_id(element)
        except Exception as e:
            L.warning(str(e))
            raise SeleniumError(str(e))

    @classmethod
    def find_element_by_name(cls, element):
        try:
            return cls.driver.find_element_by_name(element)
        except Exception as e:
            L.warning(str(e))
            raise SeleniumError(str(e))

    @classmethod
    def find_element_by_class(cls, element):
        try:
            return cls.driver.find_element_by_class_name(element)
        except Exception as e:
            L.warning(str(e))
            raise SeleniumError(str(e))

    @classmethod
    def _click_id(cls, element, x, y):
        target = cls.find_element_by_id(element)
        cls.__click_cordinate(target, x, y)

    @classmethod
    def _click_class(cls, element, x, y):
        target = cls.find_element_by_class(element)
        cls.__click_cordinate(target, x, y)

    @classmethod
    def _click_name(cls, element, x, y):
        target = cls.find_element_by_name(element)
        cls.__click_cordinate(target, x, y)

    @classmethod
    def __click_cordinate(cls, target, x, y):
        off_x = int(target.size["width"]) / 2
        off_y = int(target.size["height"]) / 2
        actions = ActionChains(cls.driver)
        actions.move_to_element(target)
        actions.move_by_offset(x - off_x, y - off_y)
        actions.click()
        actions.move_to_element(target)
        actions.perform()

    @classmethod
    def refresh(cls):
        cls.driver.navigate().refresh()

    @classmethod
    def quit(cls):
        cls.driver.quit()

if __name__ == "__main__":
    import time
    w = Selenium()
    w.start("http://www.dmm.co.jp/netgame/social/-/gadgets/=/app_id=787487/")
    time.sleep(10)
    w.find_element_by_id("login_id").send_keys("dmm.setsulla@gmail.com")
    w.find_element_by_id("password").send_keys("ztesr676")
    w.find_element_by_class("btn-login").click()
    time.sleep(10)
    w.quit()
