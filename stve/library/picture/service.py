import os
import sys

LIB_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from picture.module import Picture, __version__

class Factory(object):
    def __init__(self):
        pass

    def version(self):
        return __version__

    def get(self):
        return Picture()


NAME = "stve.picture"
FACTORY = Factory()
