# -*- coding:utf-8 -*-
# Author: Evan Mi
import multiprocessing


def f(conn):
    conn.send([42, None, 'hello from child'])
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send('hello from parent')
    p.join()
    parent_conn.close()
