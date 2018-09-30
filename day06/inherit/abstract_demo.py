# -*- coding:utf-8 -*-
# Author: Evan Mi

# -*- coding: utf-8 -*-
# Python抽象类的基本模板

from abc import ABCMeta, abstractmethod

# 定义抽象类，继承object
class People(object):
    # 定义为抽象类
    __metaclass__ = ABCMeta

    # 公有变量
    name = 'marco'
    # 私有变量，双下划线开头
    __age = 20

    def __init__(self, name = 'Mike'):
        self._name = name
        self.__age = 20

    # 如果不设置setter，则属性为只读
    # _name为可读写，而_age为只读
    @property
    def Name(self):
        print ('get name...')
        return self._name

    @Name.setter
    def Name(self, name):
        print ('set name...')
        self._name = name

    @property
    def Age(self):
        print ('get age...')
        return self.__age

    # 定义抽象方法，子类继承时需实现
    @abstractmethod
    def sayHello(self):
        pass



# 定义实现类, 继承和实现抽象类和其方法
class Student(People):
    def __init__(self, name = 'Leo'):
        self.name = name
        self.age = 18

    def sayHello(self):
        print ('Student say hello to you')

s = Student()
s.sayHello()