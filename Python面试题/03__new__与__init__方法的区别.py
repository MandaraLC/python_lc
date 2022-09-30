'''
__new__是在实例创建之前被调用的，用于创建实例，然后返回该实例对象，是个静态方法
__init__是当实例对象创建完成后被调用的，用于初始化一个类实例，是个实例方法。

也就是： __new__先被调用，__init__后被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
'''

class A():
    def __new__(cls, *args, **kwargs):
        print('this is A __new__')
        # return super(A, cls).__new__(cls)  # 或者下面这种形式，两种都可
        return object.__new__(cls)

    def __init__(self, title):
        print('this is A __init__')
        self.title = title


a = A('python book')
