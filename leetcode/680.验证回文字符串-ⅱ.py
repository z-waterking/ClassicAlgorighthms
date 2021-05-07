#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(s, left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return verify(s, left+1, right, True) or verify(s, left, right-1, True)
                else:
                    left += 1
                    right -= 1
            return True
        return verify(s, 0, len(s)-1, False)
# @lc code=end

