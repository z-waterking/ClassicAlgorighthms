#
# @lc app=LeetCode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = {}
        for c in s1:
            if c not in needs:
                needs[c] = 0
            needs[c] += 1

        cnt = 0
        l = 0
        r = 0

        while r < len(s2):
            if s2[r] in needs:
                needs[s2[r]] -= 1

                if needs[s2[r]] >= 0:
                    cnt += 1

            while r - l >= len(s1):
                if len(s1)== r-l:
                    return True
                
                # 收缩
                if s2[l] in needs:
                    needs[s2[l]] += 1
                    if needs[s2[l]] > 0:
                        cnt -= 1
                    
                l += 1    
            r += 1
        
        return False
# @lc code=end

