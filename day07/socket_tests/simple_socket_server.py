# -*- coding:utf-8 -*-
# Author: Evan Mi
import socket
import os
server = socket.socket()
server.bind(('localhost', 6969))
server.listen(2)
while True:
    conn, addr = server.accept()
    print(addr, 'is incoming ...')
    while True:
        try:
            data = conn.recv(1024)
            # 当客户端调用.close()方法后会一直接收到空数据，所以要处理
            if not data or data.decode() == '1':
                print('client has lost')
                conn.close()  # 如果客户端一直在recv的话，也会一直收到空数据
                break
            print('recv: ', data.decode(encoding='utf-8'))
            # conn.send(data.decode(encoding='utf-8').upper().encode(encoding='utf-8'))
            res = os.popen("netstat -ano").read()
            print(res)
            # conn.send(res.encode())
            conn.sendall(res.encode())
        except Exception as e:
            print(e)
        finally:
            break
server.close()
