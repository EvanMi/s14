# -*- coding:utf-8 -*-
# Author: Evan Mi
# 生成一个普通列表
my_val = [[i for i in range(10)] for j in range(10)]
print(my_val)


# 生成器
my_gen = (i*2 for i in range(10))
print(my_gen)
# 只能用for循环的方式来取，因为是一个一个生成的；
for el in my_gen:
    print(el)


# 用函数的方式来实现生成器


def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        xxx = yield b  # 后面的b在运行到yield时被带出去，前面的xx在激活yield时被带进来
        print(xxx)
        a, b = b, a+b
        n += 1
    return 'done'


gx = fib(10)
print(gx)
# for xx in gx:
#    print(xx)

while True:
    try:
        xx = next(gx)
        print('gx', xx)
    except StopIteration as e:
        print(e.value)
        break


"""
gx = fib(10)
# 一开是只能调用next，因为这时只是创建了一个生成器，还没有yield变量
print('out;', next(gx))
# 把233给yield，同时往下运行到下一次循环到yield处，并带回yield的值
print('out;', gx.send(233))
print('out;', gx.send(333))
print('out;', gx.send(433))
# 循环到下一次的yield，并带回yield的值（其实就是把None给了yield）
print('out;', next(gx))
"""