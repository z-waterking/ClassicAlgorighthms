#
# @lc app=LeetCode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l < r:
            
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
# @lc code=end

