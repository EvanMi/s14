# -*- coding:utf-8 -*-
# Author: Evan Mi
import datetime
print(datetime.datetime.now()) #  输出当前日期，时间 2018-03-03 16:51:58.265250
print(datetime.datetime.now()+datetime.timedelta(3))  # 日期加3
print(datetime.datetime.now()+datetime.timedelta(-3))  # 日期减3
print(datetime.datetime.now()+datetime.timedelta(hours=3, days=10))  # 可以指定要加减的字段，支持的字段如下
"""
days
seconds
microseconds
milliseconds
minutes
hours
weeks
"""