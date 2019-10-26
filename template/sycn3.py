#coding:utf-8
import time
import threading


def gen_coroutine(f):
    def wrapper(*args,**kwargs):
        gen_f = f()    #gen_f为生成器req_a
        r = next(gen_f)   #r是生成器long_io
        def fun(g):
            ret = g
            try:
                gen_f.send(ret)   #将结果返回给req_a并使其继续执行
            except StopIteration:
                pass
        th1 = threading.Thread(target=fun,args=(r))
        th1.start()
    return wrapper

def long_io():
    print("开始执行IO操作")
    time.sleep(5)
    print("完成IO操作yeild回调操作结果")
    yield "io result"

@gen_coroutine
def req_a():
    print("开始处理请求a")
    ret = yield long_io()
    print("ret:%s"%ret)
    print("请求a处理完成")


def req_b():
    print("开始处理请求b")
    time.sleep(2)
    print("请求b处理完成")

def main():
    req_a()
    req_b()
    while True:
        pass

if __name__ == '__main__':
    main()



