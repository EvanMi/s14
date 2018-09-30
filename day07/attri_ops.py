# -*- coding:utf-8 -*-
# Author: Evan Mi


class Dog(object):

    def __init__(self, name):
        self.__first_name = name
        self.__last_name = 'W'

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    @property
    def name(self):
        pass

    @name.setter
    def name(self, name):  # 有了setter以后，使用d.name = xx的时候就调用了setter方法
        name_lst = name.split("||")
        self.__first_name = name_lst[0]
        self.__last_name = name_lst[1]

    @name.getter
    def name(self):  # 写了getter以后，使用x = d.name的时候就是调用getter方法，而不是直接调用property方法
        print("from the getter method")
        return self.__first_name + '||' + self.__last_name

    @name.deleter
    def name(self):  # 在调用del 的时候调用这个方法了
        print("from the deleter method")

    def eat(self, food):
        print('%s is eating %s' % (self.name, food))

d = Dog('sss')
d.name = 'sss||s'
print(d.name)
del d.name
print(d.name)
