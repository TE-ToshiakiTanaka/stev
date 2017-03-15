import websocket
import thread
import time
import cv2
from StringIO import StringIO
import base64
from PIL import Image
import numpy as np
import time

def on_message(ws, message):
    img = base64.b64decode(message)
    print img

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"
    cv2.destroyAllWindows()

def on_open(ws):
    ws.send('1920x1080/0')

if __name__ == "__main__":
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9002/minicap",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              subprotocols=["binary", "base64"])
    ws.on_open = on_open
    ws.run_forever()
