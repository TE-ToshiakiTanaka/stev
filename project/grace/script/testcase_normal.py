import os
import sys
import time

from grace.utility import *
from grace.utility import LOG as L
from grace.script import testcase

class TestCase(testcase.TestCase_Base):

    def initialize(self, form=None):
        if not self.enable_timeout("home.png"):
            self.login(); self.sleep()
            while self.expedition_result(): self.sleep()
        if form == None:
            return self.enable_timeout("home.png")
        else:
            self.tap_timeout("action_formation.png"); self.sleep()
            return self.formation(form)

    def login(self):
        self.adb.stop(self.get("kancolle.app"))
        time.sleep(5)
        self.adb.invoke(self.get("kancolle.app")); self.sleep()
        self.tap_timeout("start_music_off.png", timeout=1); self.sleep()
        self.tap_timeout("start_game.png", timeout=1); self.sleep()
        return True

    def __capture_path(self):
        return os.path.join(self.get_target(self.adb.get().TMP_PICTURE))

    def expedition_result(self):
        if self.enable_timeout("expedition_result.png", loop=2, timeout=0.5):
            self.tap_timeout("expedition_result.png", self.__capture_path()); time.sleep(7)
            if self.enable_timeout("expedition_success.png", loop=2, timeout=1):
                self.slack_message(self.get("bot.expedition_success"))
            elif self.enable_timeout("expedition_failed.png", loop=2, timeout=1):
                self.slack_message(self.get("bot.expedition_failed"))
            self.tap_timeout("next.png"); self.sleep()
            self.tap_timeout("next.png", self.__capture_path()); time.sleep(2)
            fname = self.adb_screenshot(self.adb.get().TMP_PICTURE)
            if self.adb.get().LOCATE == "V": self.picture_rotate(fname, "90")
            self.picture_resize(fname, "480P")
            self.slack_upload(fname)
            self.tap_timeout("next.png"); time.sleep(2)
            return self.enable_timeout("expedition_result.png", loop=3, timeout=0.5)
        else:
            return False

    def formation(self, formation):
        self.tap_timeout("formation_change.png"); self.sleep()
        if not self.enable_timeout("formation_deploy.png", loop=3, timeout=0.5):
            return False
        if formation == None: return False
        fleet = int(formation) % 3
        if self.adb.get().LOCATE == "V":
            p = POINT(int(self.adb.get().FORMATION_X) - (int(self.adb.get().FORMATION_WIDTH) * fleet),
                      int(self.adb.get().FORMATION_Y),
                      int(self.adb.get().FORMATION_WIDTH),
                      int(self.adb.get().FORMATION_HEIGHT))
        else:
            p = POINT(int(self.adb.get().FORMATION_X),
                      int(self.adb.get().FORMATION_Y) + (int(self.adb.get().FORMATION_HEIGHT) * fleet),
                      int(self.adb.get().FORMATION_WIDTH),
                      int(self.adb.get().FORMATION_HEIGHT))
        L.info(p);
        if not self.enable_timeout("form_fleet_1_focus.png", loop=2, timeout=2):
            self.tap_timeout("form_fleet_1.png"); self.sleep()
        self.tap_timeout_crop("formation_select.png", p); self.sleep()
        time.sleep(3)
        fname = self.adb_screenshot("formation_%s.png" % self.adb.get().SERIAL)
        if self.adb.get().LOCATE == "V":
            self.picture_rotate(fname, "90")
        self.picture_resize(fname, "480P"); self.slack_upload(fname)
        return self.home()

    def home(self):
        self.tap_timeout("action_home.png"); time.sleep(3)
        return self.enable_timeout("home.png")

    def supply(self, fleet):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_supply.png"); self.sleep()
        if not self.enable_timeout(self.__fleet_focus(fleet), loop=2, timeout=0.5):
            self.tap_timeout(self.__fleet(fleet)); self.sleep()
        self.slack_message(self.get("bot.supply") % fleet)
        self.tap_timeout("supply_all.png"); self.sleep()
        return True

    def attack(self, fleet, id):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_sortie.png"); self.sleep()
        self.tap_timeout("sortie_attack.png"); time.sleep(2)
        self.__attack_stage(id)
        self.tap_timeout(self.__attack_id(id)); self.sleep()
        self.tap_timeout("attack_decide.png"); self.sleep()
        if not self.enable_timeout(self.__fleet_focus(fleet), loop=1, timeout=1):
            self.tap_timeout(self.__fleet(fleet)); time.sleep(1)
        if self.enable_timeout("attack_unable.png", loop=2, timeout=1):
            self.slack_message(self.get("bot.attack_failed"))
            self.home(); return False
        if self.enable_pattern_timeout("attack_rack*", loop=1):
            self.slack_message(self.get("bot.attack_rack")); self.home(); return True
        if self.enable_pattern_timeout("attack_damage*", loop=1):
            self.slack_message(self.get("bot.attack_damage")); self.home(); return True
        self.tap_timeout("attack_start.png"); time.sleep(10)
        self.slack_message(self.get("bot.attack_success"))
        return self.enable_timeout("attack_compass.png")
        return True

    def __attack_stage(self, id):
        if int(id) > 30: self.tap_timeout("stage_6.png", threshold=0.49); self.sleep()
        elif int(id) > 24: self.tap_timeout("stage_5.png", threshold=0.49); self.sleep()
        elif int(id) > 18: self.tap_timeout("stage_4.png", threshold=0.49); self.sleep()
        elif int(id) > 12: self.tap_timeout("stage_3.png", threshold=0.49); self.sleep()
        elif int(id) > 6: self.tap_timeout("stage_2.png", threshold=0.49); self.sleep()
        else: pass

    def __attack_id(self, id):
        return "attack_%s.png" % id

    def battle(self):
        if not self.enable_timeout("attack_compass.png"):
            if self.enable_timeout("home.png"): return True
            else: return False
        self.tap_timeout("attack_compass.png", self.__capture_path())
        while not self.enable_timeout("next.png", loop=3, timeout=2):
            if self.tap_timeout("attack_formation_1.png", self.__capture_path()):
                self.sleep(); self.adb_screenshot(self.adb.get().TMP_PICTURE)
            if self.tap_timeout("night_battle_stop.png", self.__capture_path()):
                self.sleep(); self.adb_screenshot(self.adb.get().TMP_PICTURE)
            time.sleep(10)
        while self.tap_timeout("next.png", loop=3, timeout=0.5): self.sleep(base=2)
        while not self.enable_timeout("attack_withdrawal.png", loop=3, timeout=0.5):
            if self.enable_timeout("return.png", loop=3, timeout=0.5):
                fname = self.adb_screenshot("drop_%s.png" % self.adb.get().SERIAL)
                if self.adb.get().LOCATE == "V":
                    self.picture_rotate(fname, "90")
                self.picture_resize(fname, "480P"); self.slack_upload(fname)
                self.tap_timeout("return.png", loop=3, timeout=0.5)
        self.tap_timeout("attack_withdrawal.png"); time.sleep(5)
        self.slack_message(self.get("bot.attack_return"))
        return self.enable_timeout("home.png")

    def __fleet(self, fleet):
        return "formation_fleet_%s.png" % fleet

    def __fleet_focus(self, fleet):
        return "formation_fleet_%s_focus.png" % fleet

    def supply_and_docking(self, fleet):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_supply.png"); self.sleep()
        if not self.enable_timeout(self.__fleet_focus(fleet), loop=2, timeout=2):
            self.tap_timeout(self.__fleet(fleet), self.__capture_path()); self.sleep()
        self.slack_message(self.get("bot.supply") % fleet)
        self.tap_timeout("supply_all.png"); self.sleep()
        self.tap_timeout("menu_docking.png"); self.sleep()
        self.slack_message(self.get("bot.docking"))
        for _ in range(3):
            position = self.find("docking_room.png")
            if position == None: break
            self.tap_timeout("docking_room.png", loop=2, timeout=1)
            time.sleep(3); result = self.__docking()
            self._tap(position, threshold=0.49)
            self.sleep()
            if not result: break
        fname = self.adb_screenshot("docking_%s.png" % self.adb.get().SERIAL)
        if self.adb.get().LOCATE == "V":
            self.picture_rotate(fname, "90")
        self.picture_resize(fname, "480P"); self.slack_upload(fname)
        return True

    def docking(self):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_docking.png"); self.sleep()
        self.message(self.get("bot.docking"))
        for _ in range(3):
            position = self.find("docking_room.png")
            if position == None: break
            self.tap_timeout("docking_room.png", loop=2, timeout=1)
            time.sleep(3); result = self.__docking()
            self._tap(position, threshold=0.49)
            self.sleep()
            if not result: break
        fname = self.adb_screenshot("docking_%s.png" % self.adb.get().SERIAL)
        if self.adb.get().LOCATE == "V":
            self.picture_rotate(fname, "90")
        self.picture_resize(fname, "480P"); self.upload(fname)
        return True

    def __docking(self):
        if not self.enable_timeout("docking_next.png", loop=3, timeout=1):
            return False
        p = POINT(int(self.adb.get().DOCKING_X),
                  int(self.adb.get().DOCKING_Y),
                  int(self.adb.get().DOCKING_WIDTH),
                  int(self.adb.get().DOCKING_HEIGHT))
        for _ in range(7):
            L.info(p); self.sleep(base=1)
            self._tap(p, threshold=0.49); self.sleep()
            if self.enable_timeout("docking_unable.png", loop=1, timeout=0.5):
                self.sleep(base=1); self._tap(p, threshold=0.49); self.sleep(base=1)
            elif self.tap_timeout("docking_start.png", loop=1, timeout=0.5):
                self.sleep(base=1)
                if self.tap_timeout("docking_yes.png", loop=1, timeout=0.5):
                    self.sleep(base=3); return True
            if self.adb.get().LOCATE == "V":
                p.x = int(p.x) - int(p.width)
                if int(p.x) < 0: return False
            else:
                p.y = int(p.y) + int(p.height)
                if int(p.y) > int(self.adb.get().HEIGHT): return False
        return False

    def expedition(self, fleet, id):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_sortie.png"); self.sleep()
        self.tap_timeout("sortie_expedition.png"); self.sleep()
        self.__expedition_stage(id)
        self.tap_timeout(self.__expedition_id(id)); self.sleep()
        if self.enable_timeout("expedition_done.png", loop=2, timeout=2):
            self.slack_message(self.get("bot.expedition_done") % self.get("args.fleet"))
            return True
        self.tap_timeout("expedition_decide.png"); self.sleep()
        if not self.enable_timeout(self.__fleet_focus(fleet), loop=2, timeout=2):
            self.tap_timeout(self.__fleet(fleet)); self.sleep()
        if self.enable_timeout("expedition_unable.png", loop=2, timeout=2):
            self.slack_message(self.get("bot.expedition_unable") % self.get("args.fleet"))
            self.home()
            return False
        self.tap_timeout("expedition_start.png"); self.sleep()
        if self.enable_timeout("expedition_done.png"):
            self.slack_message(self.get("bot.expedition_start") % self.get("args.fleet"))
            time.sleep(5)
            fname = self.adb_screenshot(self.adb.get().TMP_PICTURE)
            if self.adb.get().LOCATE == "V":
                self.picture_rotate(fname, "90")
            self.picture_resize(fname, "480P"); self.slack_upload(fname)
            return True
        else:
            self.slack_message(self.get("bot.expedition_unable") % self.get("args.fleet"))
            self.home()
            return False

    def __expedition_id(self, id):
        return "expedition_%s.png" % id

    def __expedition_stage(self, id):
        if int(id) > 32: self.tap_timeout("expedition_stage_5.png"); time.sleep(1)
        elif int(id) > 24: self.tap_timeout("expedition_stage_4.png"); time.sleep(1)
        elif int(id) > 16: self.tap_timeout("expedition_stage_3.png"); time.sleep(1)
        elif int(id) > 8: self.tap_timeout("expedition_stage_2.png"); time.sleep(1)
        else: pass

    def exercises(self):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_sortie.png"); self.sleep()
        self.tap_timeout("sortie_exercises.png"); self.sleep()
        self.enable_timeout("expedition.png")
        p = POINT(int(self.adb.get().EXERCISES_X),
                  int(self.adb.get().EXERCISES_Y),
                  int(self.adb.get().EXERCISES_WIDTH),
                  int(self.adb.get().EXERCISES_HEIGHT))
        target = self.adb_screenshot(self.adb.get().TMP_PICTURE)
        for _ in range(5):
            if self.enable_pattern_crop_timeout("exercises_win_*.png", p, filename=target, loop=1, timeout=1):
                L.info("I'm already fighting. I won.")
            elif self.enable_pattern_crop_timeout("exercises_lose_*.png", p, filename=target, loop=1, timeout=1):
                L.info("I'm already fighting. I lost.")
            else:
                L.info(p);
                while not self.enable_timeout("exercises_start.png", loop=2, timeout=0.5):
                    self._tap(p, threshold=0.49); time.sleep(3)
                fname = self.adb_screenshot("exercises_%s.png" % self.adb.get().SERIAL)
                if self.adb.get().LOCATE == "V":
                    self.picture_rotate(fname, "90")
                self.picture_resize(fname, "480P")
                self.tap_timeout("exercises_start.png", loop=2, timeout=0.5); self.sleep()
                if self.enable_timeout("exercises_unable.png", loop=2, timeout=0.5): return False
                self.slack_upload(fname)
                if self.tap_timeout("exercises_attack.png", loop=3, timeout=1):
                    self.slack_message(self.get("bot.exercises_start")); self.sleep()
                    while not self.enable_timeout("next.png", loop=3, timeout=2):
                        if self.tap_timeout("attack_formation_1.png", loop=3, timeout=1): self.sleep()
                        if self.tap_timeout("night_battle_start.png"):
                            self.slack_message(self.get("bot.night_battle_start"))
                            time.sleep(1)
                        time.sleep(10)
                    target = self.adb_screenshot(self.adb.get().TMP_PICTURE)
                    if self.enable_timeout("d.png", target, loop=2, timeout=1): self.slack_message(self.get("bot.result_d"))
                    elif self.enable_timeout("c.png", target, loop=2, timeout=1): self.slack_message(self.get("bot.result_c"))
                    elif self.enable_timeout("b.png", target, loop=2, timeout=1): self.slack_message(self.get("bot.result_b"))
                    elif self.enable_timeout("a.png", target, loop=2, timeout=1): self.slack_message(self.get("bot.result_a"))
                    else: self.slack_message(self.get("bot.result_s"))
                    while self.tap_timeout("next.png", loop=3, timeout=2): time.sleep(5)
                    break
            if self.adb.get().LOCATE == "V":
                p.x = int(p.x) - int(p.width); L.info("Point : %s" % str(p))
                if int(p.x) < 0:
                    fname = self.adb_screenshot("%s.png" % self.adb.get().SERIAL)
                    self.picture_rotate(fname, "90"); self.picture_resize(fname, "480P")
                    self.slack_message(self.get("bot.exercises_result"))
                    self.slack_upload(fname)
                    self.home(); return False
            else:
                p.y = int(p.y) + int(p.height); L.info("Point : %s" % str(p))
                if int(p.y) > int(self.adb.get().HEIGHT):
                    fname = self.adb_screenshot("%s.png" % self.adb.get().SERIAL)
                    self.picture_resize(fname, "480P")
                    self.slack_message(self.get("bot.exercises_result"))
                    self.slack_upload(fname)
                    self.home(); return False
        time.sleep(3)
        return self.enable_timeout("home.png")

    def quest(self):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_quest.png"); self.sleep()
        self.tap_timeout("quest_ohyodo.png"); self.sleep()
        self.adb_screenshot("capture.png")
        return True
