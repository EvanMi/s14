# -*- coding:utf-8 -*-
# Author: Evan Mi
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    # 初始化
    def setup(self):
        pass

    # 结束的时候
    def finish(self):
        pass

    def handle(self):  # 客户端所有的交互都是在handle中完成的
        while True:
            try:
                data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address))
                print(data)
                if not data:
                    print(self.client_address, "断开了")
                    break
                self.request.sendall(data.decode().upper().encode())
            except ConnectionResetError as e:
                print(e)
                break


if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999
    # 多进程 在Windows上是无法使用的，因为调用的是fork命令
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)
    # 多线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    # 单线程
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
    server.server_close()
# server.shutdown()
