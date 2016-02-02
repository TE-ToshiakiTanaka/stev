import os
import sys
import shutil
import tempfile

from stve.exception import *
from stve.log import LOG as L

class Workspace(object):
    def __init__(self, path, force=True):
        if not type(path) in [str, unicode]:
            raise WorkspaceError("WorkspaceError : path must be strings.")
        self.default_path = path
        if os.path.exists(path):
            if len(os.listdir(path)) > 0:
                L.warning("It is not vacant folder in the path.")
                if not force:
                    raise WorkspaceError(
                        "WorkspaceError : it must be vacant folder in the path.")
        else:
            self._mkdir_recursive(self.default_path)

    def _mkdir_recursive(self, path):
        sub_path = os.path.dirname(path)
        if not os.path.exists(sub_path):
            self._mkdir_recursive(sub_path)
        if not os.path.exists(path):
            os.mkdir(path)

    def mkdir(self, folder, host="", force=True):
        if not type(folder) in [str, unicode]:
            raise WorkspaceError("WorkspaceError : folder must be strings.")
        if host == "":
            path = os.path.join(self.default_path, folder)
        else:
            if not os.path.exists(host): self._mkdir_recursive(host)
            path = os.path.join(host, folder)

        if os.path.exists(path):
            if len(os.listdir(path)) > 0:
                L.warning("It is not vacant folder in the path.")
                if not force:
                    raise WorkspaceError(
                        "WorkspaceError : it must be vacant folder in the path.")
        else:
            self._mkdir_recursive(path)
        return path

    def rmdir(self, folder, host=""):
        if not type(folder) in [str, unicode]:
            raise WorkspaceError("WorkspaceError : folder must be strings.")
        if host == "":
            path = os.path.join(self.default_path, folder)
        else:
            if not os.path.exists(host):
                raise WorkspaceError(
                    "WorkspaceError : it is not exists %s" % host)
            path = os.path.join(host, folder)
        if not os.path.exists(path):
            raise WorkspaceError("WorkspaceError : it is not exists %s" % path)
        else:
            shutil.rmtree(path)
        return path

    def touch(self, filename, host=""):
        if not type(filename) in [str, unicode]:
            raise WorkspaceError("WorkspaceError : filename must be strings.")
        if host == "":
            filepath = os.path.join(self.default_path, filename)
        else:
            host = self.mkdir(host)
            filepath = os.path.join(host, filename)
        if os.path.exists(filepath):
            raise WorkspaceError("WorkspaceError : it is exists %s" % filepath)
        with open(filepath, 'a'):
            os.utime(filepath, None)
        return filepath

    def unique(self, host=""):
        if host == "": host = self.default_path
        else: host = self.mkdir(host)
        tf = tempfile.TemporaryFile(dir=host)
        return tf.name

    def rm(self, filepath):
        if not type(filename) in [str, unicode]:
            raise WorkspaceError("WorkspaceError : filepath must be strings.")
        if not os.path.exists(filepath): L.warning("it is not exists %s" % filepath)
        else: os.remove(filepath)
        return filepath
