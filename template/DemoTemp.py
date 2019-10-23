#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

def title_join(titles):
    return "_".join(titles)

class BaseHandler(tornado.web.RequestHandler):

    def __init__(self):
        pass

    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def on_finish(self):
        pass

class IndexHandler(BaseHandler):
    def get(self):
        houses = [{}]