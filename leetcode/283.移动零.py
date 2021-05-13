#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            # 移除0
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1
        
        while left < len(nums):
            nums[left] = 0
            left += 1

# @lc code=end

