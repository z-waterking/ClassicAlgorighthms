#
# @lc app=LeetCode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针
        # 双指针原地删除
        left = 0
        right = 0
        while right < len(nums):
            # 找到了一个对应元素
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
# @lc code=end

