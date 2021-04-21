#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        div = 5
        while div <= n:
            res += n//div
            div *= 5
        return res
# @lc code=end

