# -*- coding:utf-8 -*-
# Author: Evan Mi


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise MyException('我的异常')
except MyException as e:
    print(e)
