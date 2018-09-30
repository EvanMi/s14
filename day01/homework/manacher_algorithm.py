# -*- coding:utf-8 -*-
# Author: Evan Mi
import math
# 要测试的字符串
test_str = 'babad'
# enriched_len 是指#b#a#b#a#d#的长度
enriched_len = len(test_str)*2 + 1

#
radses = [0]*enriched_len

current_rights_index = 0
current_center = 0

result_rads = 0
result_center = 0

for i in range(enriched_len):   # 遍历所有增强后的字符串#b#a#b#a#d# 这里我并没有真的构建该字符串,只是假装有一个
    if current_rights_index > i:
        """
        如过i在current_rights_index的左侧，那么就可以利用预备知识（2）来确定更长的初始半径
        symmetric_i = 2*current_center - i 预备知识（1） 求出i关于current_center对称的点的下标
        radses[i] = min(radses[symmetric_i], current_rights_index - i)当i在current_rights_index的左侧时，
        预备知识
        （2）或其推论，必然有一个成立；current_rights_index - i（推论中的AN - J 由对称性 也是 I - A0）
        是推论成立时的半径，
        radses[symmetric_i]是预备知识（2）成立时的情况。这里用min，读者可以从预备知识（2）中的图上看出来，
        推论成立的时候一定是current_rights_index - i小，而反之则是radses[symmetric_i]；当然也可能一起成立，
        相等取最小也是OK的。
        """
        symmetric_i = 2*current_center - i
        radses[i] = min(radses[symmetric_i], current_rights_index - i)
    else:
        radses[i] = 0
    """
    i - (radses[i] + 1) >= 0 半径向左扩展1，不超出列表范围
    i + (radses[i] + 1) < enriched_len 半径向右扩展1，不超出列表范围
    ((i - (radses[i] + 1)) % 2 == 0 and (i + (radses[i] + 1)) % 2 == 0) 扩展后的最左端和最右端的字符都是#
    这里要说明，在给一个字符串填充#以后，所有的下标为偶数的字符都是#，大家可以自己证明。
    (test_str[math.floor((i - (radses[i] + 1))/2)] == 
    test_str[math.floor((i + (radses[i] + 1))/2)]))
    在被#号填充后的字符串中，所有不是#号的字符，也就是来自源字符串的字符的下标除以2，向下取整，就是对应
    与该字符在源字符串中的下标。
    第三和第四个条件的或组合，其实就是判断半径扩展一以后两端的字符是否相同。
    这里因为并没有真正的去用#来填充原列表，而是在想象中完成，所以我们通过第三个判断来判断在想象中填充过的
    字符串的两个对应位置是否都是#号，第四个判断条件则是判断想象中填充过的字符串的两个来自于源字符串的字符
    是否相同； 当然，你也可以真的建立一个填充过的列表，那么第三和第四条判断就变成了：
    填充过的数组[i-radses[i]] == 填充过的数组[i+radses[i]]；但是多用了n+1个空间
    """
    while i - (radses[i] + 1) >= 0 and i + (radses[i] + 1) < enriched_len and \
            (((i - (radses[i] + 1)) % 2 == 0 and (i + (radses[i] + 1)) % 2 == 0) or
             (test_str[math.floor((i - (radses[i] + 1))/2)] ==
              test_str[math.floor((i + (radses[i] + 1))/2)])):
            radses[i] = radses[i] + 1   # 两端都可以扩展，那么半径扩展1

    if current_rights_index < i + radses[i]:  # 保持current_rights_index为最右的端点
        current_rights_index = i + radses[i]
        current_center = i

    if result_rads < radses[i]:  # 保存result_rads为半径最大（也就是我们要求的最长回文串）
        result_rads = radses[i]
        result_center = i

"""
这里用到了前提（3），从填充的字符的开始和结束下标转换为源字符的开始和结束下标

解释结束下标应该为
(result_center+result_rads-1)/2向下取整，
由于在python中，为前开后闭，所以变成了
(result_center+result_rads-1+1)/2向下取整，
也就是(result_center+result_rads)/2向下取整，
"""
print(test_str[math.floor((result_center-result_rads) / 2):math.floor((result_center+result_rads)/2)])

