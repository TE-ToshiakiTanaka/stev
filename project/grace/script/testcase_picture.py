import os
import sys

from grace.utility import *
from grace.utility import LOG as L
from grace.script import testcase_base

class TestCase_Picture(testcase_base.TestCase_Unit):

    def picture_crop(self, filepath, point="", rename=""):
        try:
            pic = self.picture.open(filepath)
            if point == "":
                width, height = pic.size
                point = POINT(0, 0, width, height)
            crop_pic = self.picture.crop(pic, point)
            if rename == "": rename = filepath
            return self.picture.save(crop_pic, rename)
        except Exception as e:
            L.warning(e)

    def picture_rotate(self, filepath, rotate, rename=""):
        try:
            pic = self.picture.open(filepath)
            rotate_pic = self.picture.rotate(pic, rotate)
            if rename == "": rename = filepath
            return self.picture.save(rotate_pic, rename)
        except Exception as e:
            L.warning(e)

    def picture_resize(self, filepath, resize, rename=""):
        try:
            pic = self.picture.open(filepath)
            resize_pic = self.picture.resize(pic, resize)
            if rename == "": rename = filepath
            return self.picture.save(resize_pic, rename)
        except Exception as e:
            L.warning(e)


    def picture_is_pattern(self, reference, target):
        try:
            return self.picture.is_pattern(reference, target)
        except Exception as e:
            L.warning(e)

    def picture_find_pattern(self, reference, target):
        try:
            return self.picture.search_pattern(reference, target)
        except Exception as e:
            L.warning(e)

    def picture_get_rgb(self, filepath, point=""):
        try:
            pic = self.picture.open(filepath)
            return self.picture.get_rgb(pic, point)
        except Exception as e:
            L.warning(e)
