# -*- coding:utf-8 -*-
# Author: Evan Mi
import redis

r = redis.Redis(host='localhost', port=6379)
"""
r.set('foo', 'Bar')
print(r.get('foo').decode())
"""
"""
r.set(name='test',  # key
      value='test', # value
      ex=1,         # 过期时间（秒为单位）
      px=2000,      # 过期时间（毫秒为单位）
      nx=False,     # 如果设置为True，则只有key不存在时，当前set操作才执行
      xx=False)     # 如果设置为True，则只有key存在时，当前set操作才执行
"""
"""
# 批量设置
r.mset(k1='k1', k2='k2')
r.mset({'k3': 'k3', 'k4': 'k4'})

# 批量获取
print(r.mget('k1', 'k3', 'k4'))
"""
"""
# 返回原来的值，然后用新值进行更新
r.getset('k1', 'k5')
"""
"""
# 对获取的value进行截取，截取方式为[start,end]
print(r.getrange('k1', 0, 1))
"""
"""
# 替换字符串某个位置的值
r.setrange('ttt', 2, 'x')
print(r.get('ttt'))
"""
"""
# 修改ttt对应的字符串的对应的二进制的某个位置上的值，只能是0或1
r.setbit('ttt', 1, value=0)
print(r.get('ttt'))
# 统计字符串所对应的二进制中1个个数
print(r.bitcount('ttt'))
# 获取字符串对应的二进制的某个位置的值
print(r.getbit('ttt', 22))
"""

"""
# 自加1
r.incr('test')
# 累加指定的值
r.incrby('test', 22)
# 累加小数值
r.incrbyfloat('test', 2.2)
# 自减
r.decr('test')
"""
"""
# 给字符串后追加内容
print(r.get('ttt'))
r.append('ttt', 'xyz')
print(r.get('ttt'))
"""
