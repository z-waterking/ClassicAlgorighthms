#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#
import math
# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1)
        h = int(math.sqrt(n))
        for i in range(2, n+1):
            dp[i] = i
            for j in range(2, h+1):
                if i % j == 0:
                    dp[i] = dp[j] + dp[i//j]
                    break
        return dp[n]
        
# @lc code=end

