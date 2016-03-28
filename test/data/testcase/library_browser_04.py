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
            b = self.service["stve.browser"].get("FireFox")
            self.assertTrue(b != None)
            b.start(self.get("browser.url"))
            self.assertTrue(b.find_element_by_id("hplogo") != None)
        finally:
            if b != None:
                b.quit()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
