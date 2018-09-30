# -*- coding:utf-8 -*-
# Author: Evan Mi
"""
count = 0
while True:
    print("count:", count)
    count = count + 1
"""

for i in range(10):
    print("loop ", i)
print("------------------------------------------------------------------------------------------------")
for i in range(0, 10, 2):
    print("loop ", i)
print("------------------------------------------------------------------------------------------------")
for i in range(10):
    if i % 2 == 0:
        print("loop", i)
    else:
        continue
print("------------------------------------------------------------------------------------------------")
for i in range(10):
    print('------------------', i)
    for j in range(10):
        print(j)
        if j > 5:
            break
