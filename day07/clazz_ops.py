# -*- coding:utf-8 -*-
# Author: Evan Mi


class Dog(object):
    """类的描述信息"""
    __test_val = 'val'

    def __init__(self, name):
        self.name = name

    # 对象加括号会调用这个方法
    def __call__(self, *args, **kwargs):
        print(args, kwargs)

    # java中的toString方法
    def __str__(self):
        return self.name

    @classmethod
    def eat(cls, food: str) -> None:   # 类方法只能访问类的属性，不能访问实例对象的属性
        print('%s is eating %s' % (cls.__test_val, food))

    def my(self, va):
        print(va)

d = Dog('xs')
Dog.eat('ss')
d.eat('ss')

# 打印类的描述信息
print(Dog.__doc__)
# 打印对象属于哪个模块
print(d.__module__)
# 打印对象所属的类
print(d.__class__)
# 测试call方法
d(1, 2, 3, name='alex')
# 通过类调用，会打印类中的所有类属性和方法
print(Dog.__dict__)
# 通过实例调用，会打印实例本身的属性
print(d.__dict__)
# __str__方法，也就是toString方法
print(d)
