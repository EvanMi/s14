# -*- coding:utf-8 -*-
# Author: Evan Mi
import gevent, time


def foo():
    print('Running in foo')
    gevent.sleep(22)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(10)
    print('Implicit context switch back to bar')


def rar():
    print('Running rar')
    gevent.sleep(12)
    print('running rar again')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(rar)
])

