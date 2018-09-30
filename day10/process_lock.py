# -*- coding:utf-8 -*-
# Author: Evan Mi
import multiprocessing


def f(lock, num):
    lock.acquire()
    try:
        print('hello world', num)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = multiprocessing.Lock()
    for num in range(10):
        multiprocessing.Process(target=f, args=(lock, num)).start()