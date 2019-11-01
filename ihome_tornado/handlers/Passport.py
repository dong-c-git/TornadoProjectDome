#coding:utf-8
from tornado.web import RequestHandler
from handlers.BaseHandler import BaseHandler
from utils.session import Session
from utils.response_code import RET
from utils.commons import required_login

import re
import logging
import hashlib
import config


class RegisterHandler(BaseHandler):
    """注册"""
    def post(self):
        #获取参数
        mobile = self.json_args.get("mobile")
        sms_code = self.json_args.get("phonecode")
        password = self.json_args.get("password")
        #参数完整性检查
        if not all([mobile,sms_code,password]):
            return self.write(dict(errcode=RET.PARAMERR,errmsg="参数不完整"))
        #验证手机号位数
        if not re.match(r"^1\d{10}$",mobile):
            return self.write(dict(errcode=RET.DATAERR,errmsg="手机号格式错误"))
        #验证产品密码长度；
        #if len(password)<6
        #判断短信验证码是否正确
        if "2468" != sms_code:
            try:
                real_sms_code = self.redis.get("sms_code_%s"%mobile)
            except Exception as e:
                logging.error(e)
                return self.write(dict(errcode=RET.DBERR,errmsg="查询验证码出错"))
            #判断验证码是否过期
            if not real_sms_code:
                return self.write(dict(errcode=RET.NODATA,errmsg="验证码过期"))
            #验证验证码是否准确
            if real_sms_code != sms_code:
                return self.write(dict(errcode=RET.DATAERR,errmsg="验证码错误"))
            #删除redis中验证码：
            try:
                self.redis.delete("sms_code_%s"%mobile)
            except Exception as e:
                logging.error(e)
        #保存数据，同时判断手机号是否存在，判断根据是数据库中手机号是唯一约束
        passwd = hashlib.sha256(password+config.passwd_hash_key).hexdigest()
        sql = "insert into ih_user_profile(up_name,up_mobile,up_passwd) values(%s,%s,%s);"
        try:
            params = [mobile,mobile,passwd]
            user_id = self.db.execute(sql,params)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DATAEXIST,errmsg="手机号已经存在"))
        finally:
            #是否成功都需要关闭数据库的连接
            self.db.close()
            self.connclose()
        #用session记录用户登陆状态
        session = Session(self)
        session.data["user_id"] = user_id
        session.data["mobile"] = mobile
        session.data["name"] = mobile
        try:
            session.save()
        except Exception as e:
            logging.error(e)
        self.write(dict(errcode=RET.OK,errmsg="注册成功"))

class LoginHandler(BaseHandler):
    """登录"""
    def post(self):
        #获取参数
        mobile = self.json_args.get("mobile")
        password = self.json_args.get("password")
        #检查参数
        if not all([mobile,password]):
            return self.write(dict(errcode = RET.PARAMERR, errmsg="参数错误"))
        if not re.match(r"^1\d{10}$",mobile):
            return self.write(dict(errcode = RET.DATAERR, errmsg="手机号错误"))
        params = [mobile]
        try:
            #检查密码是否正确
            res = self.db.execute("select up_user_id,up_name,up_passwd from ih_user_profile where up_mobile=%s",params)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode = RET.DBERR, errmsg = "数据库查询异常"))
        else:
            res_user = self.db.fetchall()
        finally:
            # 是否成功都需要关闭数据库的连接
            self.db.close()
            self.connclose()
        #res_user是一个元祖,直接通过元祖操作：
        password = hashlib.sha256(password+config.passwd_hash_key).hexdigest()
        if res and res_user[0][2] == password:
            #生成session数据
            #返回客户端
            try:
                self.session = Session(self)
                self.session.data['user_id'] = res_user[0][0]
                self.session.data['name'] = res_user[0][1]
                self.session.data['mobile'] = mobile
                self.session.save()
            except Exception as e:
                logging.error(e)
            return self.write(dict(errcode=RET.OK,errmag="OK"))
        else:
            return self.write(dict(errcode=RET.DATAERR,errmsg="手机号或密码错误！"))

class LogoutHandler(BaseHandler):
    """退出登录"""
    @required_login
    def get(self):
        #清理session数据
        #session = Session(self)
        self.session.clear()
        self.write(dict(errcode=RET.OK,errmsg="退出成功"))

class CheckloginHandler(BaseHandler):
    """检查登录状态"""
    def get(self):
        #get_current_user方法在基类中已经实现，返回值是session.data(用户保存在redis中的sessions数据)
        #如果为{},意味着用户未登录，否则代表用户已经登录
        if self.get_current_user():
            self.write({'errcode':RET.OK,"errmsg":"true","data":{"name":self.session.data.get("name")}})
        else:
            self.write({'errcode':RET.SESSIONERR,'errmsg':"false"})
