# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   test.py
@USER       :   ZZZZZ
@TIME       :   2021/5/7 16:48
'''


def numTrees(n):
    # dp[i]数组含义，用i个数字可以够成多少个二叉搜索树
    dp = [0] * (n + 1)
    # 每加一个数字，分为如下几种情况：
    # 1. 加的这个数字是根，则直接dp[i-1] + 1，多一种情况
    # 2. 加的这个数字不是根，则必然作为前面所有情况的最右结点，则将前面所有情况+1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += (dp[j] + 1)

    return dp[n]

print(numTrees(3))