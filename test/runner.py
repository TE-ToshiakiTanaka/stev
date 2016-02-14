import os
import sys
import mock

import xml.etree.ElementTree as ET
from nose.tools import with_setup, raises, ok_, eq_

from stve.application import StveTestRunner
from stve.workspace import Workspace
from stve.exception import *

class TestStveTestRunner(object):
    @classmethod
    def setup(cls):
        cls.runner = StveTestRunner()
        cls.root = os.path.normpath(os.path.join(os.path.dirname(__file__)))
        cls.script_path = os.path.join(cls.root, "data", "testcase")
        cls.workspace = Workspace(os.path.join(cls.root, "workspace"))
        cls.report_path = cls.workspace.mkdir("report")
        cls.tmp_path = os.path.join(cls.root, "data", "tmp")

    @classmethod
    def teardown(cls):
        cls.workspace.rmdir("")

    def base_library_execute_success(self, testcase):
        with mock.patch('sys.argv', ['stvetestrunner.py', testcase]):
            self.runner.execute_with_report(
                testcase, self.script_path, self.report_path)
            ok_(len(os.listdir(self.report_path)) > 0)
            flag = False
            testcasename = testcase.split(".")[0]
            for f in os.listdir(self.report_path):
                if testcasename in f:
                    flag = True
                    root = ET.parse(os.path.join(self.report_path, f)).getroot()
                    ok_(root.attrib["errors"] == "0")
                    ok_(root.attrib["failures"] == "0")
            ok_(flag)
