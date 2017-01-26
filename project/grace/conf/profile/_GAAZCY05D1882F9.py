import os
import sys

PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if not PATH in sys.path:
    sys.path.insert(0, PATH)

import android_base

class _GAAZCY05D1882F9(android_base.Android):
    SERIAL = "GAAZCY05D1882F9"
    TMP_PICTURE = "%s_TMP.png" % SERIAL
    IP = ""
    PORT = ""

    NAME = "ASUS ZenFone"
    WIDTH = "1920"
    HEIGHT = "1080"
    LOCATE = "H"

if __name__ == "__main__":
    print(eval("_GAAZCY05D1882F9.%s" % "TMP_PICTURE"))
