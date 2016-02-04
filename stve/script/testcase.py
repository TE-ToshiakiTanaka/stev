import os
import sys
import imp
import time
import unittest
import argparse

from stve.log import LOG as L
from stve.exception import *

SYSTEM_LIBRARY = os.path.normpath(os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "library"))

class StveTestCase(unittest.TestCase):
    config = {}
    service = {}
    """
        TestCase_Base.
            - Parse Command Line Argument.
            - Create Service's Instance.
            - Read Config File and get value.
    """
    def __init__(self, *args, **kwargs):
        global service
        super(StveTestCase, self).__init__(*args, **kwargs)
        self.register(SYSTEM_LIBRARY)
        self.__parse()

    @classmethod
    def register(cls, host):
        if not os.path.exists(host):
            raise LibraryError("%s is not exists." % (host))
        for fdn in os.listdir(host):
            try:
                if fdn.endswith(".pyc") or fdn.endswith(".py"):
                    pass
                else:
                    sys.path.append(os.path.join(host, fdn))
                    f, n, d = imp.find_module("service")
                    module = imp.load_module("service", f, n, d)
                    cls.service[module.NAME] = module.FACTORY
                    sys.path.remove(os.path.join(host, fdn))
            except Exception as e:
                L.warning(str(e))

    @classmethod
    def set(cls, name, value):
        cls.config[name] = value

    @classmethod
    def get(cls, name):
        return cls.config[name]

    def __parse(self):
        """
            Parse Command Line Arguments.
        """
        parser = argparse.ArgumentParser()

        parser = self.arg_parse(parser)

        results = parser.parse_args()
        for k, v in vars(results).items():
            self.set("args.%s" % k, v)

    def arg_parse(self, parser):
        parser.add_argument(action='store', dest="testcase",
                            help='TestCase Name.')
        return parser


    @classmethod
    def get_service(cls, settings):
        """
            Get Service.
            in the wifi branch, Used service is there.
        """
        pass

    # temporary methods.
    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test(self):
        self.assertTrue("master" == "master")

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
