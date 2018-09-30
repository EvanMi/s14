# -*- coding:utf-8 -*-
# Author: Evan Mi


class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating ... %s' % (self.name, food))


def buck(self):
    print('%s is bucking' % self.name)


d = Dog('jack')
choice = input('>>: ').strip()
# 判断是否有属性或方法
print(hasattr(d, choice))
# 获得对象的属性或方法(如果是方法，后面加括号后调用)
func = getattr(d, choice)
func('some')
print(getattr(d, 'name'))
# 给对象添加一个方法或属性,方法或属性的名字自己起
setattr(d, 'bb', buck)
setattr(d, 'age', 22)
print(d.age)
d.bb(d)  # 动态增加的方法不会自动穿self，需要自己手动去传
# 删除对象的属性
delattr(d, 'name')
print(hasattr(d, 'name'))



