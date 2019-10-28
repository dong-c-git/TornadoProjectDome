#coding:utf-8
import os
from handlers.BaseHandler import StaticFileBaseHandler
from handlers import Passport
urls = [
    (r'/api/register',Passport.RegisterHandler),
    # StaticFileBaseHandler,
    # dict(path=os.path.join(os.path.dirname(__file__),"html"),
    #      default_filename="index.html"）
]