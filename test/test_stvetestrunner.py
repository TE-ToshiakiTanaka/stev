import os
import sys
import mock

from nose.tools import with_setup, raises, ok_, eq_

from stve.application import StveTestRunner
from stve.workspace import Workspace
from stve.exception import *

class TestStveTestRunner(object):
    @classmethod
    def setup(cls):
        cls.runner = StveTestRunner()
        cls.root = os.path.normpath(os.path.join(os.path.dirname(__file__)))
        cls.script_path = os.path.join(cls.root, "data")
        cls.workspace = Workspace(os.path.join(cls.root, "workspace"))
        cls.report_path = cls.workspace.mkdir("report")

    @classmethod
    def teardown(cls):
        cls.workspace.rmdir("")

    @with_setup(setup, teardown)
    def test_stvetestrunner_execute_success_01(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute("success.py", self.script_path, v=0)

    @with_setup(setup, teardown)
    def test_stvetestrunner_execute_success_02(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute("failed.py", self.script_path, v=0)

    @with_setup(setup, teardown)
    def test_stvetestrunner_execute_success_03(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute("notdefine.py", self.script_path, v=0)

    @with_setup(setup, teardown)
    def test_stvetestrunner_execute_success_04(self):
        self.runner.execute("notdefine", self.script_path)

    @with_setup(setup, teardown)
    @raises(TestRunnerError)
    def test_stvetestrunner_execute_failed_01(self):
        self.runner.execute("notexists.py", self.script_path)

    @with_setup(setup, teardown)
    @raises(TestRunnerError)
    def test_stvetestrunner_execute_failed_02(self):
        self.runner.execute("success.py", self.workspace.mkdir("script"))

    @with_setup(setup, teardown)
    def test_stvetestrunner_execute_with_report_success_01(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute_with_report(
                "success.py", self.script_path, self.report_path)
            ok_(len(os.listdir(self.report_path)) > 0)

    @with_setup(setup, teardown)
    def test_stvetestrunner_execute_with_report_success_02(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute_with_report(
                "failed.py", self.script_path, self.report_path)
            ok_(len(os.listdir(self.report_path)) > 0)

    @with_setup(setup, teardown)
    def test_stvetestrunner_execute_with_report_success_03(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute_with_report(
                "notdefine.py", self.script_path, self.report_path)
            ok_(len(os.listdir(self.report_path)) == 0)

    @with_setup(setup, teardown)
    def test_stvetestrunner_execute_with_report_success_04(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute_with_report(
                "notdefine", self.script_path, self.report_path)
            ok_(len(os.listdir(self.report_path)) == 0)

    @with_setup(setup, teardown)
    @raises(TestRunnerError)
    def test_stvetestrunner_execute_with_report_failed_01(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute_with_report(
                "notexists.py", self.script_path, self.report_path)

    @with_setup(setup, teardown)
    @raises(TestRunnerError)
    def test_stvetestrunner_execute_with_report_failed_02(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute_with_report(
                "success.py", self.workspace.mkdir("script"), self.report_path)

    @with_setup(setup, teardown)
    @raises(TestRunnerError)
    def test_stvetestrunner_execute_with_report_failed_03(self):
        with mock.patch('sys.argv', ['stvetestrunner.py', 'notdefine.py']):
            self.runner.execute_with_report(
                "success.py", self.script_path, os.path.join(self.workspace.root(), "hoge"))
