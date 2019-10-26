#coding:utf-8
from tornado.web import RequestHandler,StaticFileHandler
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os,time

tornado.options.define("port",default="8090",type=int,help="runserver this")
class IndexHeadler(RequestHandler):
    def get(self):
        # self.set_cookie("n1", "v1")
        # self.set_cookie("n2", "v2", path="/new", expires=time.strptime("2019-10-25 23:59:59", "%Y-%m-%d %H:%M:%S"))
        # self.set_cookie("n3", "v3", expires_days=20)
        # # 利用time.mktime将本地时间转换为UTC标准时间
        # self.set_cookie("n4", "v4", expires=time.mktime(time.strptime("2019-10-25 23:59:59", "%Y-%m-%d %H:%M:%S")))
        # self.write("OK")

        #等同于
        # self.set_header("Set-Cookie", "v5=v5 expires=Fri, 25 Oct 2019 16:03:59 GMT; Path=/")
        # self.write("OK")
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1
        self.set_secure_cookie("count", str(count))
        self.write(
            '<html><head><title>Cookie计数器</title></head>'
            '<body><h1>您已访问本页%d次。</h1>' % count +
            '</body></html>'
        )
    def post(self):
        self.write("hello xsrf_cookies")



if __name__ == '__main__':
    settings=dict(
        debug=True,
        template_path=os.path.join(os.path.dirname(__file__),"static"),
        static_path=os.path.join(os.path.dirname(__file__),"static"),
        cookie_secret="2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",
        xsrf_cookies = True
    )
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r"/",IndexHeadler)],**settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()

