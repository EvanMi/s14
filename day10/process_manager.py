# -*- coding:utf-8 -*-
# Author: Evan Mi
import multiprocessing
import os


def f(d, l):
    d[1] = '1'
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = multiprocessing.Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)
