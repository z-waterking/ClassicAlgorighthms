#
# @lc app=LeetCode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0] * (len(nums) + 1)
        res[1] = nums[0]
        for i in range(2, len(res)):
            res[i] = max(res[i-1], res[i-2] + nums[i-1])
        return res[-1]

# @lc code=end

