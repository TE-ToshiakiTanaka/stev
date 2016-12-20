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
        self.assertTrue("stve.android" in self.service.keys())
        adb = self.service["stve.android"].get(self.get("android.serial"))
        adb.snapshot("screen.png", self.get("system.tmp"))
        self.assertTrue(os.path.exists(os.path.join(self.get("system.tmp"), "screen.png")))

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
