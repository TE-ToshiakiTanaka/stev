import os
import sys
import argparse
try:
    import configparser
except:
    import ConfigParser as configparser

from stve.script import StveTestCase
from grace.utility import *
from grace.utility import LOG as L

class TestCase_Unit(StveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase_Unit, self).__init__(*args, **kwargs)
        self.get_service()
        self.get_config(self.get("args.config"))

    def arg_parse(self, parser):
        parser.add_argument(action='store', dest='testcase',
                            help='TestCase Name.')
        parser.add_argument('-m', action='store', dest='mobile',
                            help='Mobile (Android) Serial ID.')
        parser.add_argument('-d', action='store', dest='deploy',
                            help='Deploy Fleet Number.')
        parser.add_argument('-f', action='store', dest='fleet',
                            help='Fleet Number. (1 ~ 4)')
        parser.add_argument('-a', action='store', dest='attack',
                            help='Attack ID.')
        parser.add_argument('-e', action='store', dest='expedition',
                            help='Expedition ID.')
        parser.add_argument('-c', action='store', dest='config',
                            help='Configure File.')
        return parser

    @classmethod
    def get_service(cls):
        cls.adb = cls.service["stve.android"].get(cls.get("args.mobile"), PROFILE_DIR)
        cls.picture = cls.service["stve.picture"].get()

        if cls.get("args.slack") == None:
            serial = cls.get("slack.serial")
        else:
            serial = cls.get("args.slack")
        cls.slack = cls.service["stve.slack"].get(serial)

    def get_config(cls, conf=None):
        if conf == None:
            conf = os.path.join(SCRIPT_DIR, "config.ini")
        else:
            conf = conf + ".ini"
            conf = os.path.join(SCRIPT_DIR, conf)
        try:
            config = configparser.RawConfigParser()
            cfp = open(conf, 'r')
            config.readfp(cfp)
            for section in config.sections():
                for option in config.options(section):
                    cls.set("%s.%s" % (section, option), config.get(section, option))
        except Exception as e:
            L.warning('error: could not read config file: %s' % str(e))
