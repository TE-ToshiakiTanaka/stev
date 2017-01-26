import os
import sys
import time

from grace.utility import *
from grace.utility import LOG as L
from grace.script import testcase

class TestCase(testcase.TestCase_Base):
    def login(self):
        self.adb.stop(self.get("kancolle.app"))
        time.sleep(5)
        self.adb.invoke(self.get("kancolle.app")); self.sleep()
        self.tap_timeout("start_music_off.png", timeout=1); self.sleep()
        self.tap_timeout("start_game.png", timeout=1); time.sleep(5)

    def __capture_path(self):
        return os.path.join(self.get_target(self.adb.get().TMP_PICTURE))

    def expedition_result(self):
        if self.enable_timeout("expedition_result.png", loop=2, timeout=1):
            self.tap_timeout("expedition_result.png", self.__capture_path()); time.sleep(7)
