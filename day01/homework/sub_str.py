# -*- coding:utf-8 -*-
# Author: Evan Mi
import re

n = 5
s = '1'
for _ in range(n - 1):
    curr = ''
    ns = ''
    count = 0
    for tem in s:
        if curr == '':
            curr = tem
            count += 1
        elif curr == tem:
            count += 1
        else:
            ns = ns + str(count) + curr
            curr = tem
            count = 1
    ns = ns+str(count)+curr
    s = ns
print(s)
"""
def _add111(m):
    print(m)
    print(m.group(0))
    print(m.group(1))
    return str(len(m.group(0))) + m.group(1)



for _ in range(n - 1):
    s = re.sub('(.)\\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    print(s)

print(s)
"""

test = 'aabbccdd'


print(re.sub('(.)\\1*', "2", test))
print(re.findall('(.)\\1*', test))
