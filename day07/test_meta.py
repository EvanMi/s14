# -*- coding:utf-8 -*-
# Author: Evan Mi


class Meta(type):
    def __new__(mcs, *args, **kwargs):
        print('meta newing...')
        return super().__new__(mcs, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('meta calling...')
        i = cls.__new__(cls)
        i.__init__(*args, **kwargs)
        return i


class Foo(object, metaclass=Meta):

    def __init__(self, name):
        print("Foo's init")
        self.name = name

    def __new__(cls, *args, **kwargs):  # new在init之前执行，new来执行init方法，new是用来创建实例的
        print("Foo's new")
        return super(Foo, cls).__new__(cls)
       # return object.__new__(cls)  # 调用父类的__new__方法


f = Foo('alex')
print(f.name)