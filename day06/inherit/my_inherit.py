# -*- coding:utf-8 -*-
# Author: Evan Mi


class A(object):

    def __init__(self):
        print('A')


class B(object):

    def __init__(self):
        print('B')


class C(A):

    pass

# classD(A) # C D A 找init方法的顺序


class D(A):  # C A D B 找init方法的顺序

    def __init__(self):
        print('D')


class E(C, D):
    pass

x = E()