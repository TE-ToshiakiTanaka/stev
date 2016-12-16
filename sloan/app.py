import os
import time
import signal
import logging

import uuid
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
from tornado.options import define, options
from tornado.web import url

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class Application(tornado.web.Application):
    def __init__(self, **overrides):
        handlers = [
            url(r"/", MainHandler, name='index'),
        ]

        settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            #"cookie_secret":    base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            #'twitter_consumer_key': 'KEY',
            #'twitter_consumer_secret': 'SECRET',
            #'facebook_app_id': '180378538760459',
            #'facebook_secret': '7b82b89eb6aa0d3359e2036e4d1eedf0',
            #'facebook_registration_redirect_url': 'http://localhost:8888/facebook_login',
            #'mandrill_key': 'KEY',
            #'mandrill_url': 'https://mandrillapp.com/api/1.0/',

            'xsrf_cookies': False,
            'debug': True,
            'log_file_prefix': "tornado.log",
        }
        tornado.web.Application.__init__(self, handlers, **settings)



def sig_handler(sig, frame):
    logging.warning('Caught signal: %s', sig)
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)

def shutdown():
    logging.info('Stopping http server')
    server.stop()

    logging.info('Will shutdown in %s seconds ...', MAX_WAIT_SECONDS_BEFORE_SHUTDOWN)
    io_loop = tornado.ioloop.IOLoop.instance()

    deadline = time.time() + MAX_WAIT_SECONDS_BEFORE_SHUTDOWN

    def stop_loop():
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            io_loop.stop()
            logging.info('Shutdown')
    stop_loop()

def main():
    tornado.options.parse_command_line()

    global server

    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)


    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    tornado.ioloop.IOLoop.instance().start()

    logging.info("Exit...")


if __name__ == '__main__':
    main()
