#
# @lc app=LeetCode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 在子串s[i..j]中，最长回文子序列的长度为dp[i][j]
        dp = []
        n = len(s)
        for i in range(n):
            dp.append([0] * n)
            dp[i][i] = 1
        
        for i in range(n-2, -1 ,-1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
# @lc code=end

