#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针原地删除
        left = 0
        right = 0
        while right < len(nums):
            # 找到了一个新元素
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
# @lc code=end

