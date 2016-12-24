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
        try:
            self.assertTrue("stve.android" in self.service.keys())
            adb = self.service["stve.android"].get(self.get("android.serial"))
            adb.install_application(self.get("android.apk"), build=True)
            adb.exec_application(adb.get().AURA_DEBUGON, {})
        except Exception as e:
            L.warning(str(e))
            self.fail()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
