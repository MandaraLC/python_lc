from threading import Thread
from time import sleep


def myasync_test(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@myasync_test
def func_A():
    print("字符串1\n")
    sleep(2)
    print("字符串2\n")

def func_B():
    print("字符串3\n")


func_A()
func_B()
'''
加上装饰符@myasync，异步执行不会等func_A()执行完才执行func_B
'''
