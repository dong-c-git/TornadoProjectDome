#coding:utf-8
import os
from handlers.BaseHandler import StaticFileBaseHandler
from handlers import Passport
urls = [
    (r'/api/register',Passport.RegisterHandler),   #注册
    (r'/api/login',Passport.LoginHandler),         #登录
    (r'/api/logout',Passport.LogoutHandler),       #退出登录
    (r'/api/check_login',Passport.CheckloginHandler),  #登录检查

    # StaticFileBaseHandler,
    # dict(path=os.path.join(os.path.dirname(__file__),"html"),
    #      default_filename="index.html"）
]