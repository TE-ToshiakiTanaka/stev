import os
import sys

LIB_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not LIB_PATH in sys.path:
    sys.path.insert(0, LIB_PATH)

from picture import module

class Factory(object):
    def __init__(self):
        pass

    def version(self):
        return module.__version__

    #def get(self):
    #    return module.Picture()


NAME = "stve.picture"
FACTORY = Factory()
