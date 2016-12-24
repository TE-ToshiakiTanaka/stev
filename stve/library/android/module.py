import os
import sys
import time
import glob
import importlib

PROFILE_PATH = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "profile"))
if not PROFILE_PATH in sys.path:
    sys.path.insert(0, PROFILE_PATH)

from stve.log import Log
from stve.cmd import run
from stve.exception import *

TIMEOUT = 30
UIAUTOMATOR_TIMEOUT = 180
UIAUTOMATOR_PATH = "/data/local/tmp/"

ADB_ROOT = os.path.normpath(os.path.dirname(__file__))

L = Log("Android.Library.ATVE")

class AndroidBase(object):
    def __init__(self, profile, host=PROFILE_PATH):
        self.WIFI = False
        self._set_profile(profile, host)

    def _set_profile(self, name, host):
        self.profile = None
        class_name = "_" + name
        if not os.path.exists(host):
            L.warning("%s is not exists." % host)
            raise AndroidError("%s is not exists." % host)

        try:
            prof = None
            for fdn in os.listdir(host):
                if fdn.endswith(".py") and (name in fdn):
                    prof = fdn.replace(".py", "")
            if prof == None:
                L.warning("Not have a profile : %s " % name)
                class_name = "_0000000000000000"
                for fdn in os.listdir(PROFILE_PATH):
                    if fdn.endswith("_0000000000000000.py"):
                        prof = fdn.replace(".py", "")
            sys.path.append(host)
            module = importlib.import_module(str(prof))
            self.profile = getattr(module, class_name)
            self.profile.SERIAL = name
            self.profile.TMP_PICTURE = "%s_TMP.png" % name
            sys.path.remove(host)
        except Exception as e:
            sys.path.remove(host)
            L.debug('=== Error Exception ===')
            L.debug('type     : ' + str(type(e)))
            L.debug('args     : ' + str(e.args))
            L.debug('e        : ' + str(e))
            raise AndroidError(str(e))

    def get_profile(self):
        return self.profile

    def __exec(self, cmd, timeout=TIMEOUT):
        L.debug(cmd)
        result = run(cmd, timeout=timeout)
        if result != None:
            try:
                if result[0] == 0:
                    result = result[1].replace("\r", "")
                else:
                    L.warning(result[2].replace("\r",""))
                    raise AndroidError("Android Execute Failed.")
            except Exception as e:
                L.warning(str(e))
                raise e
        return result

    def _target(self):
        if not self.WIFI:
            return "-s %s " % (self.profile.SERIAL)
        else:
            return "-s %s:%s " % (self.profile.IP, self.profile.PORT)

    def _adb(self, cmd, timeout=TIMEOUT):
        if "adb" in cmd:
            L.debug("command include [adb]. : %s" % cmd)
        cmd = "adb %s" % cmd
        return self.__exec(cmd, timeout)


    def push(self, src, dst, timeout=TIMEOUT):
        L.debug("[push] : %s -> %s" % (src, dst))
        cmd = "%spush %s %s" % (self._target(), src, dst)
        return self._adb(cmd, timeout)

    def pull(self, src, dst, timeout=TIMEOUT):
        L.debug("[pull]. : %s -> %s" % (src, dst))
        cmd = "%spull %s %s" % (self._target(), src, dst)
        return self._adb(cmd)

    def shell(self, cmd, timeout=TIMEOUT):
        if "shell" in cmd:
            L.debug("command include [shell]. : %s" % cmd)
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
        L.debug(str(self._adb(cmd)))
        self.kill()
        if self.WIFI: self.tcpip()
        else: self.usb()
        self.connect()

    def remount(self):
        cmd = "%sremount " % self._target()
        L.debug(self._adb(cmd))

    def restart(self):
        cmd = "%sreboot" % self._target()
        L.debug(self._adb(cmd))

    def install(self, application, timeout=TIMEOUT):
        cmd = "%sinstall -r %s" % (self._target(), application)
        L.debug(self._adb(cmd, timeout))

    def uninstall(self, application):
        cmd = "%suninstall %s" % (self._target(), application)
        L.debug(self._adb(cmd))

    def adb(self, cmd, timeout=TIMEOUT):
        if "adb" in cmd:
            L.debug("command include [adb]. : %s" % cmd)
        cmd = "%s %s" % (self._target(), cmd)
        return self._adb(cmd, timeout)

    def wait(self, timeout=TIMEOUT):
        return self.adb("wait-for-device", timeout)

class AndroidApplication(object):
    """
        This class is not Interface of Android Module.
    """
    def __init__(self, adb):
        self._adb = adb

    def release(self, directory):
        os.chdir(directory)
        if os.name =='nt': result = run("gradlew.bat assembleRelease")
        else: result = run("./gradlew assembleRelease")

        if result[0] == 0:
            L.info(result[1].replace("\n",""))
        else:
            L.warning(result[2].replace("\n",""))
            raise AndroidError("Android Utility Re-cycle Application Build Failed.")

    def install(self, directory):
        path = os.path.join(directory, "app", "build", "outputs", "apk", "app-release.apk")
        if os.path.exists(path):
            result = self._adb.install(path, timeout=600)
            L.info(result); return result
        else:
            raise AndroidError("Android Utility Re-cycle Application Not Exists. %s " % path)


    def uninstall(self, package_name):
        result = self._adb.uninstall(package_name)
        L.info(result); return result

    def execute(self, command, bundle):
        arg = ""
        for k, v in bundle.items():
            args += " -e %s %s" % (k, v)
        result = self._adb.shell("am startservice -a %s %s" % (command, arg))
        L.info(result); return result

class AndroidUiAutomator(object):
    """
        This class is not Interface of Android Module.
    """
    def __init__(self, adb):
        self._adb = adb

    def build(self, directory):
        os.chdir(directory)
        if os.name =='nt': result = run("gradlew.bat uiautomatorbuild")
    else: result = run("./gradlew uiautomatorbuild")

        if result[0] == 0:
            L.info(result[1].replace("\n",""))
        else:
            L.warning(result[2].replace("\n",""))
            raise AndroidError("Android UiAutomator Binary for Stve Build Failed.")

    def push(self, jar):
        result = self._adb.push(jar, UIAUTOMATOR_PATH)
        return result

    def execute(self, jar, exe, bundle, timeout=UIAUTOMATOR_TIMEOUT):
        arg = ""
        for k, v in bundle.items():
            arg += " -e %s \"%s\"" %(k, v)
        cmd = "uiautomator runtest %s -c %s %s" % (jar, exe, arg)
        result = self._adb.shell(cmd, timeout)
        L.info(result); return result

class Android(object):
    def __init__(self, profile, host=PROFILE_PATH):
        self._adb = AndroidBase(profile, host)
        self._uiautomator = AndroidUiAutomator(self._adb)
        self._application = AndroidApplication(self._adb)

    def get(self):
        return self._adb.get_profile()

    def install_application(self, directory, build=False):
        if build: self._application.release(directory)
        self._application.install(directory)

    def exec_application(self, command, bundle):
        self._application.execute(command, bundle)

    def build_uiautomator(self, directory):
        self._uiautomator.build(directory)

    def push_uiautomator(self, jar):
        return self._uiautomator.push(jar)

    def exec_uiautomator(self, jar, exe, bundle):
        """
            Execute UiAutomator's method.
            :arg string jar: Jar File Name. Before Jar File Pushed by push_uiautomator().
            :arg string exe: Execute Path. ex.) com.sony.ste.lascall.generic.PINUnLock
            :arg dict bundle: Argument Dictionary. ex.) {"IP":"192.168.2.20", "Port":"22"}
            :return string: adb result.
        """
        return self._uiautomator.execute(jar, exe, bundle)

    def snapshot(self, filename, host):
        self._adb.shell('screencap -p /sdcard/%s' % (filename))
        self._adb.pull('/sdcard/%s' % (filename), host)
        self._adb.shell('rm /sdcard/%s' % (filename))
        return os.path.join(host, filename)

    def start(self, intent):
        return self._adb.shell("am start -n %s" % (intent))

    def push(self, src, dst):
        return self._adb.push(src, dst)

    def pull(self, src, dst):
        return self._adb.pull(src, dst)

    def input(self, cmd):
        if "input" in cmd:
            L.debug("command include [input]. : %s" % cmd)
        cmd = "input %s" % cmd
        return self._adb.shell(cmd)

    def am(self, cmd):
        if "am" in cmd:
            L.debug("command include [am]. : %s" % cmd)
        cmd = "am %s" % cmd
        return self._adb.shell(cmd)

    def tap(self, x, y):
        cmd = "tap %d %d" % (x, y)
        return self.input(cmd)

    def invoke(self, app):
        cmd = "start -n %s" % (app)
        return self.am(cmd)

    def keyevent(self, code):
        cmd = "keyevent %s " % (code)
        return self.input(cmd)

    def text(self, cmd):
        args = cmd.split(" ")
        for arg in args:
            self._text(arg)
            self.keyevent(self.get().KEYCODE_SPACE)

    def _text(self, cmd):
        if "text" in cmd:
            L.debug("command include [text]. : %s" % cmd)
        cmd = "text %s" % cmd
        return self.input(cmd)

    def stop(self, app):
        package = app.split("/")[0]
        cmd = "force-stop %s " % (package)
        return self.am(cmd)

if __name__ == '__main__':
    a = Android("YT911C1ZCS")
    print(a.get().SERIAL)
    #a.invoke("com.dmm.dmmlabo.kancolle/.AppEntry")
    try:
        a.snapshot("screen.png", os.path.dirname(os.path.abspath(__file__)))
    except Exception as e:
        print(str(e))
    #a.stop("com.dmm.dmmlabo.kancolle/.AppEntry")
    #print a.exec_application(a.get().AURA_DEBUGON, {})
