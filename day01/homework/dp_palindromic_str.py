# -*- coding:utf-8 -*-
# Author: Evan Mi

# 测试的字符串
str_exp = "babad"
# 用来保存动态规划过程的表 1表示true 0表示false
longest_palindromes = [[-1] * len(str_exp) for i in range(len(str_exp))]
# longest_len 用来保存最长的回文串的长度
longest_len = 1
# 从长度为1的回文子串开始填表
for p_len in range(1, len(str_exp)+1):
    for i in range(len(str_exp)):
        j = p_len + i - 1
        if j < len(str_exp):
            if i == j:
                longest_palindromes[i][j] = 1
            elif j == i + 1 and str_exp[i] == str_exp[j]:
                longest_palindromes[i][j] = 1
                longest_len = p_len
            elif j > i+1 and longest_palindromes[i+1][j-1] == 1 and str_exp[i] == str_exp[j]:
                longest_palindromes[i][j] = 1
                longest_len = p_len
            else:
                longest_palindromes[i][j] = 0
# 搜索结果表，打印出所有的最优解
for i in range(len(str_exp)):
    for j in range(len(str_exp)):
        if longest_palindromes[i][j] == 1 and j-i+1 == longest_len:
            print(str_exp[i:j+1])
