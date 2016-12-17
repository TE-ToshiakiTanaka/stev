import os
import sys
import time

from stve.log import LOG as L
from stve.script import StveTestCase


class TestCase(StveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test(self):
        try:
            self.assertTrue("stve.browser" in self.service.keys())
            b = self.service["stve.browser"].get("Chrome")
            self.assertTrue(b != None)
            b.start(self.get("browser.url"), self.get("browser.driver"))
            b.find_element_by_id("lst-ib").send_keys("stve")
            b.find_element_by_name("q").submit()
            time.sleep(5)
            self.assertTrue(b.find_element_by_id("logocont") != None)
        except Exception as e:
            L.warning(str(e))
        finally:
            b.quit()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
