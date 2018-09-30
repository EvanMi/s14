# -*- coding:utf-8 -*-
# Author: Evan Mi


# def test():
#     if 1 == 1:
#         name = 'alex'
#     print(name)
#
# test()

# def ti(age):
#     print(age)
#     age = 27
#     print(age)
#     def age():
#         pass
#     print(age)
#
# ti(3)

def get_fun():
    result = []
    for i in range(0, 10):
        def x():
            print(i)
        result.append(x)
    return result


for m in get_fun():
    m()
