# -*- coding:utf-8 -*-
# Author: Evan Mi
import select
import socket
import queue

server = socket.socket()
server.bind(('localhost', 9000))
server.listen(1000)

server.setblocking(False)  # 不阻塞

inputs = [server]
outputs = []
msg_dic = {}
while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writable, exceptional)
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dic[e]
    for r in readable:
        if r is server:  # 来了一个新连接
            conn, addr = server.accept()
            print("来了一个新的连接:", addr)
            conn.setblocking(False)
            inputs.append(conn)
            msg_dic[conn] = queue.Queue()
        else:
            try:
                data = r.recv(1024)
                print(data)
                msg_dic[r].put(data)
                outputs.append(r)
                # r.send(data)
            except Exception as e:
                inputs.remove(r)
                if r in outputs:
                    outputs.remove(r)
                del msg_dic[r]
    for w in writable:
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)
        outputs.remove(w)
