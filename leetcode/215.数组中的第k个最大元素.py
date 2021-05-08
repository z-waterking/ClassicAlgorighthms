#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 采用快速排序的思想
        left = 0
        right = len(nums) - 1
        while True:
            l = left
            r = right
            temp = nums[l]
            while l < r:
                while l < r and nums[r] <= temp:
                    r -= 1
                nums[l] = nums[r]

                while l < r and nums[l] >= temp:
                    l += 1
                nums[r] = nums[l]

            nums[l] = temp
            if l == k - 1:
                # 正好找到，返回
                return nums[l]
            elif l > k - 1:
                # 如果l比较大，则从左边去找
                right = l - 1
            else:
                left = l + 1

# @lc code=end

