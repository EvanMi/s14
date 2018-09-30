# -*- coding:utf-8 -*-
# Author: Evan Mi

tests = [1, 4, 6, 1, 9, 2, 3, 5, 7, 7, 1, 22, 52, 12, 55, 943, 12, 111, 223, 445, 233, 665, 234, 133, 331]
target = 16
result = []
tests.sort()

for i in range(len(tests)-3):
    if tests[i]*4 > target:
        break
    if i > 0 and tests[i] == tests[i-1]:
        continue

    target_three = target - tests[i]

    for j in range(i+1, len(tests)-2):
        if tests[j]*3 > target_three:
            break
        if j > i+1 and tests[j] == tests[j-1]:
            continue
        target_two = target_three - tests[j]
        lo = j+1
        hi = len(tests)-1

        if tests[lo]*2 > target_two:
            continue
        if tests[hi]*2 < target_two:
            continue
        while lo < hi:
            sum_val = tests[lo] + tests[hi]
            if sum_val == target_two:
                result.append([tests[i], tests[j], tests[lo], tests[hi]])
                lo_val = tests[lo]
                while lo < hi and tests[lo] == lo_val:
                    lo += 1
                hi_val = tests[hi]
                while lo < hi and tests[hi] == hi_val:
                    hi -= 1
            elif sum_val < target_two:
                lo += 1
            else:
                hi -= 1
print(result)
