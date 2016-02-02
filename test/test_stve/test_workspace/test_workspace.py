import os

from nose.tools import with_setup, raises, ok_, eq_

from stve.workspace import Workspace
from stve.exception import *

class TestWorkspace(object):
    @classmethod
    def setup(cls):
        cls.test_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "tmp"))
        cls.workspace = Workspace(cls.test_path)

    @classmethod
    def teardown(cls):
        cls.workspace.rmdir("")

    @with_setup(setup, teardown)
    def test_workspace_mkdir_success(self):
        reference = os.path.join(self.workspace.default_path, "test01")
        result = self.workspace.mkdir("test01")
        ok_(os.path.exists(result))
        eq_(result, reference)

    @with_setup(setup, teardown)
    @raises(WorkspaceError)
    def test_workspace_mkdir_failed(self):
        result = self.workspace.mkdir(12)
        ok_(os.path.exists(result))

    @with_setup(setup, teardown)
    def test_workspace_rmdir_success(self):
        result = self.workspace.mkdir("test01")
        ok_(os.path.exists(result))
        self.workspace.rmdir("test01")
        ok_(not os.path.exists(result))

    @with_setup(setup, teardown)
    @raises(WorkspaceError)
    def test_workspace_rmdir_failed(self):
        result = self.workspace.rmdir(12)
        ok_(os.path.exists(result))
