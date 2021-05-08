#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.bc(nums, 0)
        return self.res

    def bc(self, nums, level):
        if level == len(nums) - 1:
            self.res.append(nums[:])
            return
        
        for i in range(level, len(nums)):
            nums[i], nums[level] = nums[level], nums[i]
            self.bc(nums, level + 1)
            nums[i], nums[level] = nums[level], nums[i]

# @lc code=end

