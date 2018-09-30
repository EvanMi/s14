# -*- coding:utf-8 -*-
# Author: Evan Mi

#  元组也叫只读列表
names = ("alex", "Evan")
print(names.index("alex"))
print(names[:1])
print(names.count("Evan"))

names2 = ("alex",)

# (x, _, z) = (1, 2, 3)
# print(x)
# print(z)


x , _  ,y,_ = (2, 3, 4, 8)
print(x)
print(y)
print(_)