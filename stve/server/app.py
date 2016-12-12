from __future__ import print_function
import sys
import os

import tornado.ioloop
import tornado.httpserver
import tornado.web

from stve.define import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

def run(port):
    application = tornado.web.Application(
        [(r'.*', MainHandler), ],
        template_path = os.path.join(STVE_SERVER, "templates"),
        static_path = os.path.join(STVE_SERVER, "static"),
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)

if __name__ == "__main__":
    run(8890)
    tornado.ioloop.IOLoop.current().start()
