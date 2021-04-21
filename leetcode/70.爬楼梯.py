#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        nums = [0] * (n+1)
        nums[1] = 1
        nums[2] = 2
        i = 3
        while i < n+1:
            nums[i] = nums[i-1] + nums[i-2]
            i += 1
        return nums[n]

# @lc code=end

