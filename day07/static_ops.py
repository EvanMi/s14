# -*- coding:utf-8 -*-
# Author: Evan Mi


class Dog(object):
    x = 0

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s' % (self.name, food))

    @staticmethod
    def static_eat(food):  # 跟类和对象没有关系了,不能访问类和对象中的任何属性
        print("eating %s" % food)


d = Dog("SomeDog")
d.eat('meat')
d.static_eat('rice')
Dog.static_eat('rice')
