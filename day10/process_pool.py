# -*- coding:utf-8 -*-
# Author: Evan Mi
import multiprocessing
import time,os


def foo(i):
    time.sleep(2)
    print(os.getpid())
    return i+100


def bar(arg):
    print('-->exec done:', arg)


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)
    for i in range(10):
        pool.apply_async(func=foo, args=(i,), callback=bar)
        # pool.apply(func=foo, args=(i,))

    print('end')
    pool.close()
    pool.join()
