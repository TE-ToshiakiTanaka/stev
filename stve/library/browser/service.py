__version__ = (0, 1, 0)
import os
import sys

LIB_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from browser import module
from browser.module import Selenium

class Factory(object):
    def __init__(self):
        pass

    def version(self):
        return __version__

    def get(self, mode="FireFox"):
        return Selenium(mode)


NAME = "stve.browser"
FACTORY = Factory()
