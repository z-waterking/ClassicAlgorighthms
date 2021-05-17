#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(num + 1):
            if i & 1 == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i >> 1]
        return dp
# @lc code=end

