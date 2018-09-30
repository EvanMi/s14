# -*- coding:utf-8 -*-
# Author: Evan Mi
import math


def expandAroundCenter(left, right, s):
    """
    从left和right之间开始扩展，如果left==right
    就是以left/right为中心进行扩展
    """
    rLeft = left
    rRight = right
    while rLeft >= 0 and rRight < len(s) and s[rLeft] == s[rRight]:  # 进行扩展
        rLeft -= 1
        rRight += 1
    """
    针对于返回的长度，因为在while循环停止的时候，rLeft和rRight都已经在要求的回文串之外了
    所以回文串的长度为rRight - rLeft - 1，自己可以画个过程图，一目了然。
    """
    return rRight - rLeft - 1


s = "babad"
start = 0
end = 0

for i in range(len(s)):
    odd_len = expandAroundCenter(i, i, s)  # i为中心的扩展
    even_len = expandAroundCenter(i, i + 1, s)  # i 和 i+1之间的空隙为中心进行扩展
    lens = max(odd_len, even_len)  # 取得本次扩展的最大值
    if lens > (end-start+1):  # 如果本次的长度比记录的回文的长度也就是end-start+1大，进行替换
        # 需要注意的是，已经知道了位置i,不管是以i为中心扩展了长为lens的回文还是
        # 以i和i+1的空隙为中心扩展了长为lens的回文。下面的start和end的计算方法都成立
        start = i - math.floor((lens - 1) / 2)
        end = i + math.floor(lens/2)

print(start, ":", end)
print(s[start:end+1])
