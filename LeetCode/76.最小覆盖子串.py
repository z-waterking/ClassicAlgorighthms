#
# @lc app=LeetCode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = {}
        for c in t:
            if c not in needs:
                needs[c] = 0
            needs[c] += 1
        chars = set(t)

        cnt = 0
        l = 0
        r = 0
        I = 0
        J = 0

        min_len = len(s) + 1

        while r < len(s):
            if s[r] in chars:
                needs[s[r]] -= 1

                if needs[s[r]] >= 0:
                    cnt += 1

            while cnt == len(t):
                if r-l+1 < min_len:
                    min_len = r-l+1
                    I = l
                    J = r

                # 收缩
                if s[l] in chars:
                    needs[s[l]] += 1
                    if needs[s[l]] > 0:
                        cnt -= 1

                l += 1
                        
            r += 1
        
        if min_len == len(s) + 1:
            return ""
        return s[I:J+1]

