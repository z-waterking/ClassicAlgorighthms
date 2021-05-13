#
# @lc app=LeetCode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[pos] = nums1[m-1]
                m -= 1
            else:
                nums1[pos] = nums2[n-1] 
                n -= 1
            pos -= 1
        
        while n > 0:
            nums1[pos] = nums2[n-1]
            n -= 1
            pos -= 1



# @lc code=end

