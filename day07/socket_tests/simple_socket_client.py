# -*- coding:utf-8 -*-
# Author: Evan Mi
import socket

client = socket.socket()
client.connect(('localhost', 6969))
while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode(encoding='utf-8'))
    data = client.recv(1024)
    while data:
        print(data.decode())
        print("---------------------------------------------------")
        data = client.recv(1024)
client.close()
