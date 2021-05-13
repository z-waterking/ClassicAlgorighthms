#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # 首先认为所有的数都是质数
        dp = [True] * n
        # 把0和1标记为和数
        dp[0] = dp[1] = False
        # 开启循环
        for i in range(2, n):
            # 如果当前的数是质数
            if dp[i]:
                # 所有i的倍数都是合数
                for j in range(i*i, n, i):
                    dp[j] = False
        return sum(dp)
# @lc code=end

