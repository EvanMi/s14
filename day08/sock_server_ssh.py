# -*- coding:utf-8 -*-
# Author: Evan Mi
import socket
import os
server = socket.socket()
server.bind(('localhost', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    print('new conn:', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        print('执行指令', data.decode())
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output"
        # 如果send的长度不够一次revc，revc只会取该send的内容，不会跨到下一个send中去--理解错误
        # 需要考虑粘包的问题
        conn.send((str(len(cmd_res.encode())).encode()))
        conn.recv(1024)  # 在控制粘包的send直接加入客户端的确认操作
        conn.send(cmd_res.encode())
sever.close()
