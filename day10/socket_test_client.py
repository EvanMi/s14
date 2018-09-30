# -*- coding:utf-8 -*-
# Author: Evan Mi
import socket

HOST = 'localhost'
PORT = 8001
s = socket.socket()
s.connect((HOST, PORT))
count = 0

while True:
    msg = input('>>:').encode()
    s.sendall(msg)
    data = s.recv(1024)
    print('Received', repr(data))
    count += 1
    if count == 10:
        break

s.close()
