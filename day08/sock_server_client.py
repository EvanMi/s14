# -*- coding:utf-8 -*-
# Author: Evan Mi
import socket

client = socket.socket()
client.connect(('localhost', 9999))

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode())
    cmd_res_size = int(client.recv(1024).decode())  # 接收命令结果的长度
    print("服务端申明的长度:", cmd_res_size)
    client.send('ready to load'.encode())
    received_size = 0
    while received_size != cmd_res_size:
        data = client.recv(1024)
        received_size += len(data)

        print('客户端收到的长度累加:', received_size)
    else:
        print('receive done', received_size)
        # print(bytes('我'.encode()))
        # print(bytes('1122'.encode()))
        # print(hex(1122))
        # print(oct(1122))
        #print(bytes('1122'))

client.close()
