import threading
import time

def myasync(f):
    def wrapper(*args, **kwargs):
        thr = threading.Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
        thr.setName("方法{}".format(f.__name__))
        # thr.join()
        print("线程id={},\n线程名称={},\n正在执行的线程列表:{},\n正在执行的线程数量={},\n当前激活线程={}".format(
            thr.ident,thr.getName(),threading.enumerate(),threading.active_count(),thr.is_alive())
        )
        print("=========================================")
    return wrapper

@myasync
def test(i):
    time.sleep(2)
    print(f"打印数据：{i}\n")

for i in range(100):
    test(i)
