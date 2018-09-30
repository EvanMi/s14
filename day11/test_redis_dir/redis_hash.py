# -*- coding:utf-8 -*-
# Author: Evan Mi
import redis
r = redis.Redis(host='localhost', port=6379)
r.hset('info', 'name', 'alex')
r.hset('info', 'age', '22')
# 获得所有信息
print(r.hgetall('info'))
# 返回结果{b'age': b'22', b'name': b'alex'}

# 获得map中具体的某个KEY的val
print(r.hget('info', 'name'))
# 获得map中所有的key的列表[b'name', b'age']
print(r.hkeys('info'))
# 获得map中的所有val的列表[b'alex', b'22']
print(r.hvals('info'))
# 批量设置
r.hmset('info', {'k1': 'k1', 'k2': 'k2'})
# 批量获取
print(r.hmget('info', 'k1', 'k2'))
# 获取map的大小
print(r.hlen('info'))
# 某个key是否存在
print(r.hexists('info', 'k1'))
# 删除某个key
# print(r.hdel('info', 'k2'))
# 给map中的某个key的val增加一定的值
r.hincrby('info', 'age', 22)
r.hincrbyfloat('info', 'age', 2.2)
# 进行过滤
print(r.hscan('info', 0, 'k*', 1))
# 生成一个过滤后的迭代器
print(r.hscan_iter('info', 'k*'))