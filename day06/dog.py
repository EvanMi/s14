# -*- coding:utf-8 -*-
# Author: Evan Mi


class Dog:
    total_num = 0  # 所有对象公用的，节省内存开销

    def __init__(self, name):
        self.name = name
        self.__life = 100  # 私有属性
        Dog.total_num += 1

    def __sub_life(self):
        self.__life -= 10

    def show_life(self):
        self.__sub_life()
        return self.__life

    def bulk(self):
        print('%s wang wang wang' % self.name)

    @classmethod
    def add_total(cls):
        cls.total_num += 1

    @classmethod
    def sub_total(cls):
        cls.total_num -= 1

    def __del__(self):
        Dog.total_num -= 1
        print('%s said: 886' % self.name)


d1 = Dog('dog1')
d1.name = 'gos'
d1.age = True   # 给d1添加age属性，值为True

d1.total_num = 200  # 并没有修改Dog的total_num，而是给d1添加了一个total_num，值为200

d2 = Dog('dog2')
d3 = Dog('dog3')


d1.bulk()
d2.bulk()
d3.bulk()
print(Dog.total_num)
del d1
print(Dog.total_num)
