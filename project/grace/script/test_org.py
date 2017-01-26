import os
import sys
import time

from grace.utility import *
from grace.utility import LOG as L
from grace.script import testcase_normal

class TestCase(testcase_normal.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test_1(self):
        L.info("*** Test 01 ***")
        #self.login()
        #self.expedition_result()
        self.adb_screenshot("capture.png")

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
