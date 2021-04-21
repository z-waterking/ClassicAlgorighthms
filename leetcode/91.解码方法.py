#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        pre = ord(s[0]) - ord('0')
        if pre == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [1] * (n + 1)
        for i in range(2, n+1):
            cur = ord(s[i-1]) - ord('0')
            if (pre == 0 or pre > 2) and cur == 0:
                return 0
            
            if (pre < 2 and pre > 0) or (pre == 2 and cur < 7):
                if cur != 0:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1]
            pre = cur
        return dp[n]
# @lc code=end

