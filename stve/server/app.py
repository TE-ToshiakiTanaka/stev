from __future__ import print_function
import sys
import os
from multiprocessing import Process

import tornado.ioloop
import tornado.httpserver
import tornado.web

from stve.define import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

class Server(object):
    def __init__(self, port=8888):
        self.application = tornado.web.Application(
            [(r'.*', MainHandler), ],
            template_path = os.path.join(STVE_SERVER, "templates"),
            static_path = os.path.join(STVE_SERVER, "static"),
        )

        def server_thread(application, port):
            http_server = tornado.httpserver.HTTPServer(application)
            http_server.listen(port)
            tornado.ioloop.IOLoop.instance().start()

        self.process = Process(target=server_thread,
                                args=(self.application, port, ))

    def start(self):
        self.process.start()

    def stop(self):
        ioloop = tornado.ioloop.IOLoop.instance()
        ioloop.add_callback(ioloop.stop)

if __name__ == "__main__":
    server = Server(8891)
    server.start()
    time.sleep(10)
    server.stop()
