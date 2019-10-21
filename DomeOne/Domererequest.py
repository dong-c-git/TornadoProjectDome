#coding:utf-8
from tornado.web import RequestHandler
import tornado.ioloop
import tornado.httpserver
import tornado.options
import re

tornado.options.define("port",default=8090,type=int,help="this is runserver")
class IndexHandler(RequestHandler):
    """正则请求相关练习"""
    def get(self):
        self.write("index OK")

class SubjectCityHandler(RequestHandler):
    def get(self,subject,city):
        self.write("subject:%s<br>City%s"%(subject,city))

class SubjectDataHandler(RequestHandler):
    def get(self,date,subject):
        self.write(("Date:%s<br>subject:%s"%(date,subject)))



if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r'/',IndexHandler),
                                   (r'/sub-city/(.+)/([a-z]+)',SubjectCityHandler),
                                   (r'/sub_date/(?P<subject>.+)/(?P<date>\d+)',SubjectDataHandler),
                                   ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()

