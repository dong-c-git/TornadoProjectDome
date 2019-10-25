#coding:utf-8
import pymysql
from tornado.web import RequestHandler,StaticFileHandler
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os


def title_join_test(str):
    return str
tornado.options.define("port",default="8090",type=int,help="runserver")
class IndexHandler(RequestHandler):
    def get(self):
        self.cs1 = self.application.conn.cursor()
        ret = self.cs1.execute("select * from tbl_user_info;")
        for i in range(ret):
            result = self.cs1.fetchone()
            print(result)
        print(ret)
        # self.write("sql select")
        self.render("index.html",houses=result,title_join=title_join_test)

class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            database="itcast",
            user="root",
            password="root",
            charset="utf8"
        )

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application([(r"/",IndexHandler)],
                      template_path=os.path.join(os.path.dirname(__file__),"static"),
                      debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()
