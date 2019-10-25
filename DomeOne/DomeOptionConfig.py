#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
#from tornado.options import options,parse_command_line,parse_config_file
#py通过导入方式加载文件中的配置：
import config

tornado.options.define("port",default="8090",type=int,help="run server on the givent port")
tornado.options.define("hello",default=[],type=str,multiple=True,help="this hello test")
# options.logging=None    #设置不打印日志
# parse_command_line()
class IndexHandler(tornado.web.RequestHandler):
    """首页页面"""
    def get(self):
        self.write("hello world this is tornado")


if __name__ == '__main__':
    tornado.options.parse_config_file("./config")
    print(tornado.options.options.hello)
    app1 = tornado.web.Application([],**config.settings)
    print(app1)
    app = tornado.web.Application([(r'/',IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()