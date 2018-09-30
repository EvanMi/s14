# -*- coding:utf-8 -*-
# Author: Evan Mi
import selectors
import socket

sel = selectors.DefaultSelector()   # 默认使用epoll,如果不支持epoll，就会使用select


def accept(sock, mask):
    conn, addr = sock.accept()
    print('接收连接', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    print(mask)
    data = conn.recv(1024)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        print('closing ', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 8869))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
