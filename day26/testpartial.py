# -*- coding:utf-8 -*-
# Author: Evan Mi
from functools import partial


def sum(x, y, z):
    return x + y - z


sum_2 = partial(sum, 2)

print(sum_2(3, 1))

sum_1 = partial(sum, 2, 3)

print(sum_1(1))

sum_sum = partial(sum, 2, z=2)

print(sum_sum(y=3))
