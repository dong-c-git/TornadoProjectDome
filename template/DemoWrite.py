#coding:utf-8
from  tornado.web import RequestHandler
import tornado.ioloop
import tornado.options
import tornado.httpserver
import pymysql
import os

#数据库链接insert数据
class IndexHandler(RequestHandler):
    def get(self):
        self.set_cookie("itcase","abcd")
        self.write("aaaaa")

class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        self.db = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            database="itcast",
            user="root",
            password="mysql"
        )

if __name__ == '__main__':
    tornado.options.command_line()
    current_path = os.path.dirname(__file__)
    settings = dict(
        
    )
