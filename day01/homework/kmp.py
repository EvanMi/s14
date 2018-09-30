# -*- coding:utf-8 -*-
# Author: Evan Mi


def kmp(haystack, needle):
    slen = len(haystack)
    plen = len(needle)
    nexts = [0] * plen
    get_next(needle, nexts)
    print(nexts)
    i = 0
    j = 0
    while i < slen and j < plen:
        if haystack[i] == needle[j] or j == -1:
            i += 1
            j += 1
        else:
            j = nexts[j]-1

    if j == plen:
            return i-j
    else:
        return -1


def get_next(needle, nexts):
    al = len(needle)
    nexts[0] = 0
    k = -1
    j = 0
    while j < al - 1:
        if k == -1 or needle[j] == needle[k]:
            j += 1
            k += 1
            nexts[j] = k+1
        else:
            k = nexts[k]-1


print(kmp("mississippi", "mississippi"))