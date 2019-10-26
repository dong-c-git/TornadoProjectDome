#coding:utf-8
from tornado.web import RequestHandler,StaticFileHandler
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.httpclient
import os,json

tornado.options.define("port",default="8090",type=int,help="runserver")
class IndexHandler(RequestHandler):

    #@tornado.web.asynchronous
    # @tornado.web.gen.coroutine
    # def get(self):
    #     http = tornado.httpclient.AsyncHTTPClient()
    #     http.fetch("http://www.ip138.com/ips138.asp?ip=58.60.2.178",callback=self.on_response)
    #
    # def on_response(self,response):
    #     if response.error:
    #         self.send_error(500)
    #     else:
    #         self.write(response.body)
    #     self.finish()
    @tornado.web.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://www.ip138.com/ips138.asp?ip=58.60.2.178")
        if response.send_error:
            self.send_error(500)
        else:
            self.write(next(response))

if __name__ == '__main__':
    settings=dict(
        template_path=os.path.join(os.path.dirname(__file__),"static"),
        static_path=os.path.join(os.path.dirname(__file__),"static"),
        debug=True,
        cookie_secret="2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",
        xsrf_cookies=True,

    )
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r"/",IndexHandler)],**settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()
