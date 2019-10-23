#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

tornado.options.define("port",default="8090",type=int,help="runserver")
class IndexHandler(tornado.web.RequestHandler):
    """接口调用顺序"""
    def initialize(self):
        print("调用了initialize")

    def prepare(self):
        print("调用了prepare")

    def set_default_headers(self):
        print("调用了set_default_hansers")

    def write_error(self,status_code,**kwargs):
        print("调用了write_error")

    def get(self):
        print("调用了get请求")

    def post(self):
        print("调用了post请求")
        self.send_error(400)

    def on_finish(self):
        print("调用了on_finish()")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r'/',IndexHandler)],debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()