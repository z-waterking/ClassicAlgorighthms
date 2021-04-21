#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = -max(prices)-1
        for price in prices:
            dp_i_1 = max(dp_i_1, -price)
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
        return dp_i_0
# @lc code=end

