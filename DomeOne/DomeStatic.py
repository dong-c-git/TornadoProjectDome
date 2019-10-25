#coding:utf-8
from tornado.web import RequestHandler,StaticFileHandler
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os


def house_title_join(titles):
    return "+".join(titles)

#static_path使用提供功能有限；
#StaticFileHandler支持正则和字典参数
tornado.options.define("port",default="8090",type=int,help="runserver")
class IndexHandler(RequestHandler):
    def get(self):
        # print(self.static_url("html"))
        #构造需要渲染的数据：
        house_info = {
            "price": 3980000,
            "title": "宽窄巷子+160平大空间+文化保护区双地铁",
            "score": 5,
            "comments": 6,
            "position": "北京市丰台区六里桥地铁"
        }
        houses = [
            {
                "price": 4580000,
                "title": "宽窄巷子+文化保护区双地铁",
                "score": 6,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 99980000,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 999990000,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 10,
                "position": "北京市丰台区六里桥地铁"
            }
        ]
        #render返回渲染数据
        # self.render("index.html",houses=houses)
        #self.render("index-1.html",text="")
        self.render("index.html",houses=houses,title_join = house_title_join)


    def post(self):
        text = self.get_argument("text", "")
        print(text)
        self.render("index-1.html", text=text)


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r"/",IndexHandler,),
                                   (r"/i/()$",StaticFileHandler,{"path":os.path.join(current_path,"static"),"default_filename":"index.html"}),
                                   ],
                                  static_path=os.path.join(os.path.dirname(__file__),"static"),
                                  template_path = os.path.join(os.path.dirname(__file__),"static"),
                                  debug=True,
                                  autoescape=None
                                  )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()