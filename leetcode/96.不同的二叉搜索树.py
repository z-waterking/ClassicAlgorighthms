#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i]数组含义，用i个数字可以够成多少个二叉搜索树
        # 每加一个数字，分为如下几种情况：
        # 1. 加的这个数字是根，则直接dp[i-1] + 1，多一种情况
        # 2. 加的这个数字不是根，则必然作为前面所有情况的最右结点，则将前面所有情况+1
        
        # 只有一个结点时，必然是1
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                # 左子树的可能组合和右子树的可能组合
                # 1-j为左子树结点个数
                # i-1-j为右子树结点个数
                dp[i] += dp[j] * dp[i-1-j]
        return dp[n]

# @lc code=end

