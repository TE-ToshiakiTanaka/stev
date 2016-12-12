import sys
from websocket import create_connection
ws = create_connection("ws://localhost:8889/websocket")

if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    message = 'hogehogehoge'

print ws.send(message)
print ws.recv()

ws.close()
