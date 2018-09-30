# -*- coding:utf-8 -*-
# Author: Evan Mi
import socket
import time
client = socket.socket()
client.connect(('localhost', 8869))
while True:
    msg = input('>>:').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode())
    data = client.recv(1024)
    print('recv:', data.decode())
