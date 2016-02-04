import os
import sys
import imp
import csv
import unittest
import xmlrunner

from stve.log import LOG as L
from stve.exception import *

class StveTestRunner(object):
    def __init__(self):
        pass

    def load(self, testcase):
        if testcase.find(".py") != -1:
            script = testcase
        else:
            script = testcase + ".py"
        path = os.path.join(host, script)
        if not os.path.exists(path):
            raise TestRunnerError("%s is not exists." % (path))
        name = script[:script.find(".")]
        L.debug("TestCase : %s" % path)
        if os.path.exists(path):
            f, n, d = imp.find_module(str(name))
            return imp.load_module(name, f, n, d)
        else:
            return False

    def execute(self, script, host):
        if not os.path.exists(host):
            raise TestRunnerError("%s is not exists." % (host))
        sys.path.append(host)

        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        module = self.load(script)
        if not module:
            L.warning("Not loaded module : %s" % script)
        else: suite.addTest(loader.loadTestsFromModule(module))
        unittest.TextTestRunner(verbosity=2).run(suite)

    def execute_with_report(self, script, host, output):
        if not os.path.exists(host):
            raise TestRunnerError("%s is not exists." % (host))
        sys.path.append(host)

        if not os.path.exists(output):
            raise TestRunnerError("%s is not exists." % (output))

        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        module = self.load(script)
        if not module:
            L.warning("Not loaded module : %s" % script)
        else: suite.addTest(loader.loadTestsFromModule(module))
        xmlrunner.XMLTestRunner(output=output).run(suite)
