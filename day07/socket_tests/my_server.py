# -*- coding:utf-8 -*-
# Author: Evan Mi
import socket

server = socket.socket()
server.bind(('localhost', 11221))
server.listen()

conn, addr = server.accept()


data = conn.recv(1024)
print(data)
conn.close()

server.close()