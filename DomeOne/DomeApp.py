#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define,options
from tornado.web import RequestHandler,url

tornado.options.define("port",default="7890",type=int,help="runserver this is help")

class IndexHandler(tornado.web.RequestHandler):
    """首页访问文件"""
    def get(self):
        self.write("hello this is my first app")

class IndexHandler(RequestHandler):
    """主页请求"""
    def get(self):
        self.write('<a herf="'+self.reverse_url("cpp_url")+'">cpp</a>')

class SubjectHandler(RequestHandler):
    def initialize(self,subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    print(tornado.options.options.port)
    app = tornado.web.Application([(r'/',IndexHandler),
                                   (r'/python',SubjectHandler,{"subject":"python"}),
                                   url(r"/cpp",SubjectHandler,{"subject":"cpp"},name="cpp_url"),
                                   ],
                                  debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
