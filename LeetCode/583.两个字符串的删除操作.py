#
# @lc app=LeetCode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 先找最长公共子序列
        dp = []
        for i in range(len(word1) + 1):
            dp.append([0] * (len(word2) + 1))
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return len(word1) + len(word2) - 2 * dp[len(word1)][len(word2)]
# @lc code=end

