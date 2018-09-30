# -*- coding:utf-8 -*-
# Author: Evan Mi


class Foo(object):
    """my Foo class"""
    def __getitem__(self, item):
        print('__getitem__', item)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()
# 调用对象的__setitem__
obj['name'] = 'alex'
# 调用对象的__getitem__
print(obj['name'])
# 调用对象的__delitem__
del obj['name']
