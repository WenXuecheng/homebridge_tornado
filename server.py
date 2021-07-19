import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

import config
from application import Application

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options["port"])
    httpServer.start(0)
    tornado.ioloop.IOLoop.current().start()
