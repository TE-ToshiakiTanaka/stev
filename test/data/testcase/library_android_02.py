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
        self.assertTrue("stve.android" in self.service.keys())
        self.assertTrue(self.service["stve.android"].version() != None)
        L.info(self.service["stve.android"].version())

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
