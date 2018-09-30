# -*- coding:utf-8 -*-
# Author: Evan Mi
import socket
import time
client = socket.socket()
client.connect(('localhost', 11221))
client.send("2323".encode())
while True:
    data = client.recv(1024)
    print(data)

time.sleep(5)
client.close()