#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

#options处理获取参数
tornado.options.define("port",default=8090,type=int,help="run server on the givent port")
tornado.options.define("hello",default=[],type=str,multiple=True,help="hello is test help")
class IndexHandler(tornado.web.RequestHandler):
    """首页函数"""
    def get(self):
        """处理get请求"""
        self.write("hello world tornado")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    print(tornado.options.options.hello)
    app = tornado.web.Application([(r'/',IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()