import os
import sys
import time

from ida.utility import *
from ida.utility import LOG as L
from ida.script import testcase_base

class TestCase(testcase_base.TestCase_Unit):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test_hello(self):
        L.info("*** Test Hello ***")
        self.assertTrue(1 == 1)

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
