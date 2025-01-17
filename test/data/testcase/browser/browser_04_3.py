import os
import sys
import time

from stve.log import LOG as L
from stve.exception import *
from stve.script import StveTestCase


class TestCase(StveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test(self):
        try :
            self.assertTrue("stve.browser" in self.service.keys())
            b = self.service["stve.browser"].get("Chrome")
            self.assertTrue(b != None)
            b.start(self.get("browser.url"), self.get("browser.driver"))
            self.assertTrue(b.find_element_by_id("hplogo") != None)
        except Exception as e:
            L.warning(str(e))
            self.fail()
        finally:
            b.quit()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
