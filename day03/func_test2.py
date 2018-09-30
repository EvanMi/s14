# -*- coding:utf-8 -*-
# Author: Evan Mi


def add(x, y, f):
    return f(x) + f(y)


def sub_one(x, y, f):
    return f(x, y, abs)-1


res = sub_one(3, -6, add)
print(res)
