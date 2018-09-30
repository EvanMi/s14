# -*- coding:utf-8 -*-
# Author: Evan Mi

# 函数


def func1():
    print('in the func1')
    return 0

# 过程


def func2():
    print('in the func2')

"""
多个值用逗号分割后返回，会分装到一个tuple中返回，
接收的时候，如果使用一个变量接收，那么这个接收变量就是一个tuple类型的
如果接收的时候也用逗号分割多个值来接收，那么可以分别对应返回tuple中的每一个值
"""


def func3():
    return 1, 'hello', ['alex', 'wupei'], {'name': 'alex'}

x = func1()
y = func2()
z = func3()  # 一个值接收，是一个tuple
q, w, e, r = func3()  # 用对应个数的值接收，每个变量对应tuple对应位置的值
print(x)
print(y)
print(z)

print("center".center(100, '*'))
print(q)
print(w)
print(e)
print(r)

print("center".center(100, '*'))

# 定义一个方法


def test(x_arg, y_arg):
    print(x_arg)
    print(y_arg)


test(1, 2)  # 位置参数调用
test(y_arg=3, x_arg=5)  # 关键字参数调用，直接给形式参数赋值


def test1(x_arg, y_arg, z_arg):
    print(x_arg)
    print(y_arg)
    print(z_arg)


#  关键字参数不能写到位置参数之前
test1(1, z_arg=2, y_arg=3)


# 默认值参数
def test2(x_arg, y_arg=2):
    print(x_arg)
    print(y_arg)


print("center".center(100, '*'))
test2(1)
print("center".center(100, '*'))
test2(1, 3)
print("center".center(100, '*'))
test2(y_arg=5, x_arg=8)

"""
在*args 前面有参数(x, *args)，那么(1,2,3,4,5)正确，(x=1,2,3,4,5)正确，(2,3,4,5,x=1)错误，给x多次赋值了
在*args 后面有参数(*args,x,y)那么x,y只能采用关键字赋值方式(1,2,3,4,5,x=6,y=8) 
"""


def test3(*args):
    print(args)


test3(1, 2, 3, 4, 5)
test3(*[1, 2, 3, 4, 5])
print("center".center(100, '*'))


def test4(x_arg, *args):
    print(x_arg)
    print(args)


test4(1, 2, 3, 4, 5)


def test5(**kwargs):
    print(kwargs)
    print(kwargs['name'])


test5(name='alex', age=8)
test5(**{'name': 'Evan', 'age': 8})


def test6(*args, xx):
    print(args)
    print(xx)

#  **kwargs 必须在最后
#   def test7(**kwargs,xx=3): 这样定义是错误的


print("test6")
# test6(1, 2, 3, 4, 5999, xx=4)
"""
*args 接收位置参数，转换为tuple
**kwargs 接收关键字参数，转换为dict
位置参数不能写在关键字参数的后面
"""


def tt(xx=1, *args, **kwargs):
    print(xx)
    print(args)
    print(kwargs)


def ttt(xx, **kwargs):
    print(xx)
    print(kwargs)


def tttt(*args, xx, **kwargs):
    print(args)
    print(xx)
    print(kwargs)

#  kwargs接收的关键字参数的名字不能和函数列表中已有的其他参数相同
#  tt(2, 3, 4, 5, name=100, age=199, xx=98)
# 出现了xx，优先赋值给参数列表中的xx，而不是在dict中加入关键字为xx的key-value对
# ttt(x=99, y=99, xx=43)

tttt(1,2,3,4,5,x=100,y=33,xx=8)