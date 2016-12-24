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
            L.info(self.get("android.jar"))
            L.info(adb.build_uiautomator(self.get("android.jar")))
            L.info(adb.push_uiautomator(os.path.join(self.get("android.jar"), 'bin', adb.get().JAR_AUBS)))
            L.info(adb.exec_uiautomator(adb.get().JAR_AUBS, adb.get().AUBS_SYSTEM_ALLOWAPP, {}))
        except Exception as e:
            L.warning(str(e))
            self.fail()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
