# -*- coding:utf-8 -*-
# Author: Evan Mi
import time
# 获得时间戳,当前时区的
print(time.time())
# 不传参数获得格林威治时间tuple，传入秒数的话就是把秒数转为tuple
print(time.gmtime())
# 不传参数将获得当前时区的时间tuple,传入秒数的话就是把秒数转为tuple
print(time.localtime())
"""
time.struct_time(tm_year=2018, tm_mon=4, tm_mday=4, tm_hour=8, tm_min=47, tm_sec=57, tm_wday=2, tm_yday=94, tm_isdst=0)
可以通过time.localtime().tm_year 或其他字段来直接获得相应字段的值
"""
# 把元组转为秒
x = time.gmtime(1245554451)
print(time.mktime(x))
# 字符串格式的日期
print(time.strftime('%Y-%m-%d %H:%M:%S | %A | %a', time.localtime()))
# 字符串转换为tuple日期
print(time.strptime('2018-02-13 17:10:23 | Tuesday | Tue', '%Y-%m-%d %H:%M:%S | %A | %a'))
# tuple时间转字符串
print(time.asctime(x))
# 秒时间转字符串
print(time.ctime(time.time()))
