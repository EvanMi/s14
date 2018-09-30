# -*- coding:utf-8 -*-
# Author: Evan Mi
import random
# 产生一个 >=0 并且 <1 的随机浮点数
print(random.random())
"""
Get a random number in the range [a, b) or [a, b] depending on rounding.
获得一个[1,3)或者[1,3]范围内的随机浮点数，在哪个范围内依赖与rounding
"""
print(random.uniform(1, 3))
# 产生一个 >=1 并且 <=3 的随机整数
print(random.randint(1, 3))
# 从1开始进行随机次数的+3操作；结果要小于5
print(random.randrange(1, 5, 3))
# 从给定的字符串、列表、元组中随机挑选一个值
print(random.choice([1, 5, 9, 6, 3]))
# 从给定的序列中（字符串、列表、元组）随机取指定个数的样本
print(random.sample('hello', 2))
x = [1, 2, 3, 4, 5, 6]
# 打乱顺序，就像洗牌一样
random.shuffle(x)
print(x)
