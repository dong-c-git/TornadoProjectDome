#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import json

#set_default_headers方法
#set_status状态码设置
#redirect跳转
tornado.options.define("port",default="8090",type=int,help="this is runserver")
class IndexHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        print("执行了set default_headers")
        #设置get和post方式的默认响应格式为json
        self.set_header("itcast","python")

    def get(self):
        stu = {
            "name":"zhangsan",
            "age":18,
            "gender":1,
        }
        # res = json.dumps(stu)

        # self.write(res)
        self.write(stu)
        self.set_header("Content-Type","application/json charset=UTF-8")
        self.write("ok 01")
        self.write("ok 02")
        self.write("ok 03")
        #设置状态码：
        self.set_status(404)

    def post(self):
        print("执行了 post请求")
        #设置post请求方式
        stu = {
            "name":"zhangsan",
            "age":24,
            "gender":1,
        }
        stu_json = json.dumps(stu)
        self.set_header("itcast","post")
        self.write(stu_json)
        self.set_status(210,"itcast error")  #非标准状态码

class Err211Handler(tornado.web.RequestHandler):
    """对应/err/211"""
    def get(self):
        self.write("hello itcast")
        self.set_status(211)  #非标准状态码，未设置reason会报错

#redirect跳转：
class IndexHandler(tornado.web.RequestHandler):
    """对应/"""
    def get(self):
        self.write("主页")
        # self.send_error(404,content="出现404错误")
        #默认的write\_error()方法
        # 不会处理send\_error抛出的kwargs参数，
        # 即上面的代码中content="出现404错误"是没有意义的。
        err_code = self.get_argument("code",None)
        err_title = self.get_argument("title","")
        err_content = self.get_argument("content","")
        if err_code:
            self.send_error(int(err_code),title=err_title,content=err_content)
        else:
            self.write("主页")

    def write_error(self,status_code,**kwargs):
        self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
        self.write(u"<p>错误名：%s</p>"%kwargs["title"])
        self.write(u"<p>错误详情：%s</p>"%kwargs["content"])

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<form method = "post"><input type="submit" value="登陆"></form>')
        self.write("主页")
        # self.send_error(404,content="出现404错误")
        self.write("结束")
        #send_error()方法后就不要再向输出缓冲区写内容了！

    def post(self):
        self.redirect("/")



if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r'/',IndexHandler),
                                   (r'/err/211',Err211Handler),
                                   (r'/login',LoginHandler)],debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()

