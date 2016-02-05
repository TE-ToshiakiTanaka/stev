import os
import sys
import time

from stve.log import Log
from stve.script import StveTestCase


class TestCase(StveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        print("*** Start TestCase   : %s *** " % __file__)

    def test(self):
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        print("*** End TestCase     : %s *** " % __file__)
