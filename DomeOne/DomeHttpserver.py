#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    """主路由器处理类"""
    def get(self):
        """对应http请求的get方法"""
        self.write("hello world tornado")

if __name__ == '__main__':
    app = tornado.web.Application([(r'/',IndexHandler)])
    #修改此部分代码
    #app.listen(8090)
    http_server = tornado.httpserver.HTTPServer(app)
    #http_server.listen(8090)
    http_server.bind(8090)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()