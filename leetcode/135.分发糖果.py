#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        cans = [1] * len(ratings)
        for i in range(len(cans) - 1):
            if ratings[i+1] > ratings[i]:
                cans[i+1] = cans[i] + 1
        
        for i in range(len(cans)-1, 0, -1):
            if ratings[i-1] > ratings[i] and cans[i-1] <= cans[i]:
                cans[i-1] = cans[i] + 1
        
        return sum(cans)
# @lc code=end

