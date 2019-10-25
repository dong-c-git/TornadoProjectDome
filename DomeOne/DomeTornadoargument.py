#coding:utf-8
from tornado.web import RequestHandler
import tornado.ioloop
import tornado.options
import tornado.httpserver

#获取各请求中的参数处理：
tornado.options.define("port",default=8090,type=int,help="runserver aways")

class IndexHandler(RequestHandler):
    """首页处理"""
    def post(self):
        query_arg = self.get_query_argument("a")
        query_args = self.get_query_arguments("a")
        print(query_arg,type(query_arg))
        print(query_args,type(query_args))
        #query_body_arg = self.get_body_argument("a")
        query_body_args = self.get_body_arguments("b")
        query_strip_args = self.get_body_arguments("c",strip=True)
        #print(query_body_arg,type(query_body_arg))
        print(query_body_args,type(query_body_args))
        print(query_strip_args,type(query_strip_args))

        print(">>>>>>>>")
        arg_argument = self.get_argument("test")
        args_argument = self.get_arguments("one",strip=False)
        print("arg_argument:",arg_argument,type(arg_argument))
        print("args_argument",args_argument,type(args_argument))
        print(self.request.headers["Content-Type"])
        print(self.request.body)
        self.write("OK")

class UpdowloadFile(RequestHandler):
    """上传文件类参数读取"""
    def post(self):
        up_file = self.request.files
        image_file = up_file.get("imgge")
        print(image_file)
        if image_file:
            image_file = image_file[0]["body"]
            file = open("./testup.png","wb+")
            file.write(image_file)
            file.close()
        self.write("OK!")


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r'/up',UpdowloadFile),(r'/',IndexHandler)],debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()


