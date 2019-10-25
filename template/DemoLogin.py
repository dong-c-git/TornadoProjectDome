#coding:utf-8
from tornado.web import RequestHandler,StaticFileHandler
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os

#登陆验证机制
tornado.options.define("port",default="7890",type=int,help="runserver")
class IndexHandler(RequestHandler):

    def get_current_user(self):
        login_url = self.get_argument("f",None)
        if login_url:
            return True
        else:
            return False

    @tornado.web.authenticated
    def get(self):
        self.xsrf_token
        #self.render("index.static")
        self.write("this is index")

    def post(self):
        self.write("aaaa")

class LoginHandler(RequestHandler):
    def get(self):
        next_url = self.get_argument("next","")
        if next_url:
            self.redirect(next_url+"?f=login")
        else:
            self.write("logined")


class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(StaticFileHandler,self).__init__(*args,**kwargs)
        self.xsrf_token
        self.set_secure_cookie("itcast","abc")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    current_path = os.path.dirname(__file__)
    settings = dict(
        template_path = os.path.join(os.path.dirname(__file__)),
        cookie_secret = "abcdefght",
        login_url = "/login",
        debug =True

    )
    app =tornado.web.Application([(r'/',IndexHandler),
                                  (r'/login',LoginHandler),
                                  (r'/(.*)',StaticFileHandler,{"path":os.path.join(os.path.dirname(__file__),"static")})
                                  ],**settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()
