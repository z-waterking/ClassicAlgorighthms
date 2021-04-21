#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c ** 0.5)
        while l <= r:
            sum = l * l + r * r
            if sum < c:
                l += 1
            elif sum > c:
                r -= 1
            else:
                return True
        return False

# @lc code=end

