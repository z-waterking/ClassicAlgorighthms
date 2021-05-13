#
# @lc app=LeetCode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
            
        left = 0
        right = len(height) - 1

        l_max = height[left]
        r_max = height[right]

        res = 0

        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res
# @lc code=end

