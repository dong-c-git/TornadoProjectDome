#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import datetime
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler

tornado.options.define("port",default=8090,type=int)

class IndexHandler(RequestHandler):
    def get(self):
        self.render("Webindex.html")

class ChatHandler(WebSocketHandler):
    users = set()   #用来存放在线用户的容器

    def open(self):
        self.users.add(self)
        for u in self.users:
            u.write_message(u"[%s]-[%s]-进入聊天室"%(self.request.remote_ip,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def on_message(self,message):
        for u in self.users:
            u.write_message(u"[%s]-[%s]-说：%s"%(self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    def on_close(self):
        self.users.remove(self)
        for u in self.users:
            u.write_message(u"[%s]-[%s]-离开聊天室"%(self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def check_origin(self,origin):
        return True

if __name__ == '__main__':
    settings = dict(
        static_path = os.path.join(os.path.dirname(__file__),"static"),
        template_path = os.path.join(os.path.dirname(__file__),"static"),
        debug = True,
    )
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r"/",IndexHandler),
                                   (r"/chat",ChatHandler),
                                   ],**settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()