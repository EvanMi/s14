# -*- coding:utf-8 -*-
# Author: Evan Mi
import redis
r = redis.Redis(host='localhost', port=6379)
# 清空列表
r.delete('names')
# 列表中添加数据,从左面添加
r.lpush('names', 'Alex', 'Evan', 'Andy', 'Bob', 'Marry')
# 列表中添加数据，从右面添加
r.rpush('names', 'Lucy', 'Lily')
# 如果队列'names'存在，就从左边添加数据
r.lpushx('names', 'left')
# 如果队列'names'存在，就从右边添加数据
r.rpushx('names', 'right')
# 查看列表中所有的值
print(r.lrange('names', 0, -1))
# 在指定值的前面或后面插入一个值
r.linsert('names', 'BEFORE', 'Marry', 'Jerry')
r.linsert('names', 'AFTER', 'Marry', 'Tom')
# 修改指定位置的值
r.lset('names', 2, 'JERRY')
print(r.lrange('names', 0, -1))
# 删除列表中指定val的值，可以指定删除的个数
r.lrem('names', 'Jerry', 2)
print(r.lrange('names', 0, -1))
# 返回列表中指定下标的值
print(r.lindex('names', 1))
# 查看列表的长度
print(r.llen('names'))
# 从左侧弹出一个元素
print(r.lpop('names'))
# 从右侧弹出一个元素
print(r.rpop('names'))
# 移除不再start和end之间的所有值
r.ltrim('names', 0, 2)
# 从names右边弹出一个值，放到names1中
print(r.rpoplpush('names', 'names1'))
# 从names右侧弹出然后放入names1左侧；如果names为空，等待超时时间
r.brpoplpush('names', 'names2', 3)
# 返回列表中的第一个元素，如果没有元素等待指定超时时间
print(r.blpop('names', 3))




