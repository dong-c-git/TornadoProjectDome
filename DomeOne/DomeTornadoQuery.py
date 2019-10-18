#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
from tornado.web import MissingArgumentError
import tornado.httpserver

tornado.options.define("port",default=8090,type=int,help="need runserver give port")

class IndexHandler(tornado.web.RequestHandler):
    """访问首页"""
    # def get(self):
    #     #     self.write("hello this is tornado server")

    def post(self):
        query_arg = self.get_query_argument("a")
        query_args = self.get_query_arguments("a")
        body_arg = self.get_body_argument("a")
        body_args = self.get_body_arguments("a",strip=False)
        arg = self.get_argument("a")
        args = self.get_argumens("a")
        default_arg = self.get_argument("b","itcast")
        default_args = self.get_arguments("b")

        try:
            missing_arg = self.get_argument("c")
        except MissingArgumentError as e:
            missing_arg = "we catched the MissingArgumentError"
            print(e)
        missing_args = self.get_arguments("c")

        rep = "query_arg:%s<br/>" % query_arg
        rep += "query_args:%s<br/>" % query_args
        rep += "body_arg:%s<br/>" % body_arg
        rep += "body_args:%s<br/>" % body_args
        rep += "arg:%s<br/>" % arg
        rep += "args:%s<br/>" % args
        rep += "default_arg:%s<br/>" % default_arg
        rep += "default_args:%s<br/>" % default_args
        rep += "missing_arg:%s<br/>" % missing_arg
        rep += "missing_args:%s<br/>" % missing_args

        self.write(rep)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r"/",IndexHandler),])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()

