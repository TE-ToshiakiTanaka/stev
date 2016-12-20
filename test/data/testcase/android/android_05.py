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
        L.info("Android Serial : %s" % adb.get().SERIAL)
        self.assertEqual(adb.get().SERIAL, self.get("android.serial"))

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
