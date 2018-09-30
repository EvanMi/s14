# -*- coding:utf-8 -*-
# Author: Evan Mi
import redis
r = redis.Redis(host='localhost', port=6379, db=12)

#  添加元素
r.zadd('z_name1', lucy=1.1, lily=2.2, evan=10)
# 查看全部元素
print(r.zrange('z_name1', 0, -1))
# 查看全部元素带分数
print(r.zrange('z_name1', 0, -1, withscores=True))
# 查看有序集合中的元素个数
print(r.zcard('z_name1'))
# 获取分数在[min,max]之间的个数
print('zcount:', r.zcount('z_name1', 0, 3))
# 自增val对应的分数
r.zincrby('z_name1', 'lucy', 2)
# 获取某个val的排名
print('zrank:', r.zrank('z_name1', 'lily'))
# 根据排名或score删除
r.zremrangebyrank('z_name1', 1, 3)
r.zremrangebyscore('z_name1', 2.3, 4.5)
print(r.zscore('z_name1', 'lily'))

#   获取两个有序集合的交集，如果遇到val相同的，则按照aggregate进行操作
# aggregate的值为:SUM MIN MAX
r.zadd('n1', alex=10, jack=5, lucy=88)
r.zadd('n2', alex=10, jack=20)
r.zinterstore('n3', ['n1', 'n2'], aggregate='MAX')
print(r.zrange('n3', 0, -1, withscores=True))
r.zunionstore('n4', ['n1', 'n2'], aggregate='SUM')
print(r.zrange('n4', 0, -1, withscores=True))

# r.keys('*')
# r.randomkey() 随机
# 从一个库移动到另一个库
# r.move()
# r.dbsize() 查询库中key的个数
# r.flushdb() 清空数据库