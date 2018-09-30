# -*- coding:utf-8 -*-
# Author: Evan Mi
import shelve
"""
shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，
可以持久化任何pickle可支持的python数据格式
"""
# d = shelve.open('my_shelve')


# class Test(object):
#     def __init__(self, n):
#         self.n = n


# t = Test(123)
# t2 = Test(122233)
#
# name = ['alex', 'rain', 'test']
# d['test'] = name
# d['t1'] = t
# d['t2'] = t2
#
# d.close()

d = shelve.open('my_shelve')

print(d.get('test'))

d.close()
