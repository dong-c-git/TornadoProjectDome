#coding:utf-8
import time
import threading

#回调版本
def login_io(cb):
    def fun(callback):
        print("开始执行耗时操作")
        time.sleep(5)
        print("耗时操作执行完成")
        result = "io result"
        callback(result)
    ret1 = threading.Thread(target=fun,args=(cb,))
    ret1.start()

def on_finish(ret):
    print("开始执行回调函数")
    print(ret)
    print("完成执行回调函数")

def req_a():
    print("开始处理请求a")
    login_io(on_finish)
    print("请求a处理完成")

def req_b():
    print("开始处理请求b")
    print("请求b处理完成")

def main():
    req_a()
    req_b()
    while True:
        pass

if __name__ == '__main__':
    main()
