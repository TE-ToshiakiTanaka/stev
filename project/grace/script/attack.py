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

    def test_attack(self):
        L.info("*** Attack ***")
        self.assertTrue(self.initialize(self.get("args.deploy")))
        while self.expedition_result(): time.sleep(2)
        self.slack_message(self.get("bot.attack"))
        self.assertTrue(self.attack(self.get("args.fleet"), self.get("args.attack")))
        self.assertTrue(self.battle())
        while self.expedition_result(): time.sleep(2)
        self.assertTrue(self.supply_and_docking(self.get("args.fleet")))
        self.assertTrue(self.home())
        while self.expedition_result(): time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
