#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = len(text1)
        y = len(text2)
        res = 0
        dp = []
        for i in range(x + 1):
            dp.append([0] * (y + 1))
        
        for i in range(1, x+1):
            for j in range(1, y+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[i][j]
# @lc code=end

