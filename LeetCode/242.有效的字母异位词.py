#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 统计一下所有字母的个数
        # 对于s，加字母
        # 对于t, 减字母
        if len(s) != len(t):
            return False

        counts = [0] * 26
        
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        if counts.count(0) == 26:
            return True
        else:
            return False

# @lc code=end

