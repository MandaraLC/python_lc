

'''
#普通模式

class Notsingleton:
    def __init__(self):
        self.user = 'admin'

    def dosomething(self):
        print(self.user)

a = Notsingleton()
b = Notsingleton()

print(a==b) #False
'''

#单例模式
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

a = Singleton()
b = Singleton()
print(a == b) #Ture

