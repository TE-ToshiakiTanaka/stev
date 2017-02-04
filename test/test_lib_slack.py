import os
import sys
import platform
from stve.log import LOG as L
from stve.script import StveTestCase
from nose.tools import with_setup, raises, ok_, eq_

LIB_PATH = os.path.dirname(os.path.abspath(__file__))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from runner import TestStveTestRunner as TSTR

class TestSlackTestRuner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_slack_success_01(self):
        self.script_path = os.path.join(self.script_path, "slack")
        self.base_library_execute_success("slack_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_slack_success_02(self):
        self.script_path = os.path.join(self.script_path, "slack")
        self.base_library_execute_success("slack_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_slack_success_03(self):
        self.script_path = os.path.join(self.script_path, "slack")
        self.base_library_execute_success("slack_03.py")
