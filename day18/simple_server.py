# -*- coding:utf-8 -*-
# Author: Evan Mi
from wsgiref.simple_server import make_server


def run_server(evviron, stat_response):
    stat_response('200 OK', [('Content-Type', 'text/html')])
    return ["<h1>Hello World</h1>".encode('utf-8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print('Server HTTP on port 8000')
    httpd.serve_forever()
