#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        flag = 0
                    else:
                        flag = 1
                    dp[i][j] = min(dp[i-1][j-1] + flag, dp[i-1][j] + 1, dp[i][j-1] + 1)
        
        return dp[m][n]
                    
# @lc code=end

