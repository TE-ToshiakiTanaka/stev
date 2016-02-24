__version__ = (0, 1, 0)

import os
import sys
import imp
import time
import glob

PROFILE_PATH = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "profile"))
if not PROFILE_PATH in sys.path:
    sys.path.insert(0, PROFILE_PATH)

from stve.log import Log
from stve.cmd import run
from stve.exception import *

TIMEOUT = 30

class AndroidBase(object):
    L = Log("Android.Library.STVE")

    def __init__(self, profile, host=PROFILE_PATH):
        self.WIFI = False
        self._set_profile(profile, host)

    def _set_profile(self, name, host):
        self.profile = None
        class_name = "_" + name
        if not os.path.exists(host):
            self.L.warning("%s is not exists." % host)
            raise AndroidError("%s is not exists." % host)

        try:
            prof = None
            for fdn in os.listdir(host):
                if fdn.endswith(".py") and (name in fdn):
                    prof = fdn.replace(".py", "")
            if prof == None:
                self.L.warning("Not have a profile : %s " % name)
                class_name = "_0000000000000000"
                for fdn in os.listdir(PROFILE_PATH):
                    if fdn.endswith("_0000000000000000.py"):
                        prof = fdn.replace(".py", "")
            f, n, d = imp.find_module(str(prof))
            module = imp.load_module(prof, f, n, d)
            self.profile = getattr(module, class_name)
            self.profile.SERIAL = name
            self.profile.TMP_PICTURE = "%s_TMP.png" % name
        except Exception as e:
            self.L.debug('=== Error Exception ===')
            self.L.debug('type     : ' + str(type(e)))
            self.L.debug('args     : ' + str(e.args))
            self.L.debug('message  : ' + e.message)
            self.L.debug('e        : ' + str(e))
            raise AndroidError(str(e))

    def get_profile(self):
        return self.profile

    def __exec(self, cmd, timeout=TIMEOUT):
        result = run(cmd, timeout=timeout)
        if result != None:
            try:
                result = result[1].decode("utf-8")
            except Exception as e:
                self.L.warning(str(e))
        return result

    def _target(self):
        if not self.WIFI:
            return "-s %s " % (self.profile.SERIAL)
        else:
            return "-s %s:%s " % (self.profile.IP, self.profile.PORT)

    def _adb(self, cmd, timeout=TIMEOUT):
        if "adb" in cmd:
            self.L.debug("command include [adb]. : %s" % cmd)
        cmd = "adb %s" % cmd
        return self.__exec(cmd, timeout)

    def _adb_dump(self, cmd, timeout=TIMEOUT):
        if "adb" in cmd:
            self.L.debug("command include [adb]. : %s" % cmd)
        cmd = "adb %s" % cmd
        return self.__exec_dump(cmd, timeout)


    def push(self, src, dst, timeout=TIMEOUT):
        self.L.debug("[push]. : %s -> %s" % (src, dst))
        cmd = "%spush %s %s" % (self._target(), src, dst)
        return self._adb(cmd, timeout)

    def pull(self, src, dst, timeout=TIMEOUT):
        self.L.debug("[pull]. : %s -> %s" % (src, dst))
        cmd = "%spull %s %s" % (self._target(), src, dst)
        return self._adb(cmd)

    def shell(self, cmd, timeout=TIMEOUT):
        if "shell" in cmd:
            self.L.debug("command include [shell]. : %s" % cmd)
        cmd = "%sshell %s" % (self._target(), cmd)
        return self._adb(cmd, timeout)

    def kill(self):
        cmd = "kill-server"
        return self._adb(cmd)

    def connect(self):
        if self.WIFI:
            cmd = "connect %s:%s" % (self.profile.IP, self.profile.PORT)
            return self._adb(cmd)

    def disconnect(self):
        if self.WIFI:
            cmd = "disconnect %s:%s" % (self.profile.IP, self.profile.PORT)
            return self._adb(cmd)

    def usb(self):
        if self.WIFI:
            self.disconnect()
            self.WIFI = False
        cmd = "%susb" % (self._target())
        return self._adb(cmd)

    def tcpip(self):
        if not self.WIFI:
            self.disconnect()
            self.WIFI = True
        cmd = "tcpip %s" % (self.profile.PORT)
        return self._adb(cmd)

    def root(self):
        cmd = "%sroot " % self._target()
        self.L.debug(str(self._adb(cmd)))
        self.kill()
        if self.WIFI: self.tcpip()
        else: self.usb()
        self.connect()

    def remount(self):
        cmd = "%sremount " % self._target()
        self.L.debug(self._adb(cmd))

    def restart(self):
        cmd = "%sreboot" % self._target()
        self.L.debug(self._adb(cmd))

    def install(self, application, timeout=TIMEOUT):
        cmd = "%sinstall -r %s" % (self._target(), application)
        self.L.debug(self._adb(cmd, timeout))

    def uninstall(self, application):
        cmd = "%suninstall %s" % (self._target(), application)
        self.L.debug(self._adb(cmd))

    def adb(self, cmd, timeout=TIMEOUT):
        if "adb" in cmd:
            self.L.debug("command include [adb]. : %s" % cmd)
        cmd = "%s %s" % (self._target(), cmd)
        return self._adb(cmd, timeout)

    def wait(self, timeout=TIMEOUT):
        return self.adb("wait-for-device", timeout)


if __name__ == '__main__':
    a = AndroidBase("38721d016004334")
    print a.profile.SERIAL
