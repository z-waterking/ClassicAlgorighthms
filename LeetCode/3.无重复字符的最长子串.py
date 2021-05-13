#
# @lc app=LeetCode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        nows = {}
        for c in s:
            if c not in nows:
                nows[c] = 0

        while right < len(s):
            c = s[right]
            nows[c] += 1
            right += 1

            while nows[c] > 1:
                d = s[left]
                left += 1
                nows[d] -= 1
            
            res = max(res, right - left)
        return res


# @lc code=end

