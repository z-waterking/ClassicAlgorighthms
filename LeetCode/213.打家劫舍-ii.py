#
# @lc app=LeetCode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
            
        return max(self.rob2(nums[1:]), self.rob2(nums[:-1]))
    
    def rob2(self, nums):
        res = [0] * (len(nums) + 1)
        res[1] = nums[0]
        for i in range(2, len(res)):
            res[i] = max(res[i-1], res[i-2] + nums[i-1])
        return res[-1]
# @lc code=end

