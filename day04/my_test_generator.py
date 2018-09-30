# -*- coding:utf-8 -*-
# Author: Evan Mi

# 引用别人的斐波那契数列生成函数
"""函数运行到yield的时候，就会暂停，并将yield关键字之后的值传到函数外，函数暂停在这里，直到等到下一次迭代"""
def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'

# 定义了一个生成器，这个生成器每次迭代得到的值就是yield带出来的值


fb = fib(10)

#  用for循环迭代
for val in fb:
    print(val)
"""
运行结果：
1
1
2
3
5
8
13
21
34
55
"""
# 用next迭代
fb1 = fib(10)
while True:
    try:
        print(next(fb1))
    except StopIteration as e:
        print(e.value)
        break
"""
运行结果：
1
1
2
3
5
8
13
21
34
55
done
"""