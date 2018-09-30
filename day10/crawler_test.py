# -*- coding:utf-8 -*-
# Author: Evan Mi
from urllib import request
import gevent
from gevent import monkey
monkey.patch_all()  # 把当前程序的所有IO操作做上标记


def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    # ff = open('url.html', 'wb')
    # ff.write(data)
    # ff.close()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/')
])
