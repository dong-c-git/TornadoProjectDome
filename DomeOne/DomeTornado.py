#coding:utf-8
import tornado.web    #tornadoweb框架和核心模块
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    """主页处理"""

    def get(self):
        """get请求方式"""
        self.write("hello world,this is tornado")

if __name__=="__main__":
    app = tornado.web.Application([(r"/",IndexHandler)])
    app.listen(8090)
    tornado.ioloop.IOLoop.current().start()

