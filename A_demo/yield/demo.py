def test():
    yield test2()

def test2():
    yield "test2"

# print(test())
# 这是一个生成器对象 <generator object test at 0x0000013BD4C32B30>

for i in test():
    print(i)
    for a in i:
        print(a)


'''
什么是生成器(generator)

大家知道，Python中一切皆是对象，生成器也不例外。实际上，生成器也是一种迭代器(iterator)，
它可以看成是迭代器对象的一种特殊情形。例如，通过以下代码我们可以定义一个可迭代对象“MyRange”。

'''
