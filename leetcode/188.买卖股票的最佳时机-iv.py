#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        dp_0 = [0] * (k+1)
        dp_1 = [-max(prices)-1] * (k+1)

        for price in prices:
            for i in range(1, k+1):
                dp_0[i] = max(dp_0[i], dp_1[i] + price)
                dp_1[i] = max(dp_1[i], dp_0[i-1] - price)
        return dp_0[k]

# @lc code=end

