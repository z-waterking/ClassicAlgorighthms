#
# @lc app=LeetCode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                if i >= len(word) and s[i-len(word):i] == word:
                    dp[i] = dp[i] or dp[i-len(word)]
        return dp[n]
# @lc code=end

