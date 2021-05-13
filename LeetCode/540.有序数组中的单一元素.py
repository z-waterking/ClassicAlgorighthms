#
# @lc app=LeetCode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            # 对于偶数
            mid = 2 * ((lo + hi) // 4)
            # 如果与后面一个数字的相等，则表明前面没有单独的元素
            if nums[mid] == nums[mid+1]:
                lo = mid+2
            # 否则，表明
            else:
                hi = mid
        return nums[lo]
# @lc code=end

