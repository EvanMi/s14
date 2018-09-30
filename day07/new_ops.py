# -*- coding:utf-8 -*-
# Author: Evan Mi


class Foo(object):
    """所有的类都是type类的实例,都是有type的构造方法创建的"""

    __metaclass__ = type  # 指定类的父类（必须是type的子类）

    def __init__(self, name):
        print("Foo's init")
        self.name = name

    def __new__(cls, *args, **kwargs):  # new在init之前执行，new来执行init方法，new是用来创建实例的
        print("Foo's new")
        return super(Foo, cls).__new__(cls)
       # return object.__new__(cls)  # 调用父类的__new__方法


f = Foo('alex')
print(f.name)

"""通过type来创建一个类开始"""
def func(self):
    print('hello Alex')
    print(self.name, self.age)
def myinit(self,name,age):
    self.name = name
    self.age = age
Foo1 = type('Fool', (object,), {'func': func,'__init__':myinit})
print(type(Foo1))
f1 = Foo1('alex', 22)
f1.func()
"""通过type来创建一个类结束"""
