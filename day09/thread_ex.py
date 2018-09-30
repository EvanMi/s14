# -*- coding:utf-8 -*-
# Author: Evan Mi
import threading


def run(n):
    print('task', n)

"""
由于存在GIL，在python中永远只能有一个线程在执行；线程锁的作用只是在线程释放了GIL锁的时候（执行100次货进行IO），
其他线程无法执行
"""
t1 = threading.Thread(target=run, args=('t1',))
t2 = threading.Thread(target=run, args=('t2',))
t1.start()
t2.start()
