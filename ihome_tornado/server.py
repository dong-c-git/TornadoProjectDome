#coding:utf-8

#服务启动入口
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os
import pymysql
import config
import redis

from handlers import Passport
from urls import urls
from tornado.options import options,define

tornado.options.define('port',default='8090',type=int,help="runserver on the given port")

class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        self.redis = redis.StrictRedis(**config.redis_options)
        self.db = pymysql.connect(**config.mysql_config)

def main():
    options.log_file_prefix = config.log_path
    options.logging = config.log_level
    tornado.options.parse_command_line()
    app = Application(
        urls,
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
