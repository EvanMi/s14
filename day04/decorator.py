# -*- coding:utf-8 -*-
# Author: Evan Mi
import time


def timmer(func):

    def warpper(*args, **kwargs):
        star_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('the func run time is %s' % (stop_time-star_time))
    return warpper


@timmer
def test1():
    time.sleep(3)
    print('in the tset1')


test1()


@timmer
def test2(name, age):
    print('test2', name, age)


test2('Evan', 12)
