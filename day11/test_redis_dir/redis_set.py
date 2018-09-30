# -*- coding:utf-8 -*-
# Author: Evan Mi
import redis
r = redis.Redis(host='localhost', port=6379)
# 向集合中添加多个值,重复的值会被覆盖
r.sadd('set_name', 'alex', 'Evan', 'alex', 'jerry', 'Tom', 'Marry')
r.sadd('set_name1', 'alex', 'Evan')
# 获取集合中元素的个数
print(r.scard('set_name'))
# 查看集合中的值
print(r.smembers('set_name'))
# 求一个集合和其他集合的差集
print(r.sdiff('set_name', 'set_name1'))
# 求一个集合和其他集合的差集并保存到新的集合中
print(r.sdiffstore('set_name2', 'set_name', 'set_name1'))
print(r.smembers('set_name2'))
# 求一个集合和其他集合的交集
print(r.sinter('set_name', 'set_name1'))
# 求一个集合和其他集合的交集,并保存到新的集合中
r.sinterstore('set_name4', 'set_name', 'set_name1')
print(r.smembers('set_name4'))
# 集合中是否有指定的值
print(r.sismember('set_name', 'alex'))
# 把一个值从一个集合移动到另外一个集合中
r.smove('set_name2', 'set_name3', 'alex')
# 从集合的右侧弹出一个值
print(r.spop('set_name4'))
# 从集合中随机获取指定个数的元素
print(r.srandmember('set_name1', 2))
# 从集合中删除某些值
r.srem('set_name4', 'alex', 'Even')
# 求一个集合与其他集合的并集
print(r.sunion('set_name', 'set_name1', 'set_name2'))
# 求一个集合与其他集合的并集，并保存到新的集合中
r.sunionstore('set_name5', 'set_name', 'set_name1', 'set_name2')
print(r.smembers('set_name5'))
# 扫描
print(r.sscan('set_name5', 0, 'j*'))
# 扫描为一个迭代器
r.sscan_iter('set_name5', 'j*')
