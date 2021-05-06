
#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        W = sum(nums)
        if W % 2 != 0:
            return False
        W = W // 2
        
        dp = []
        for i in range(N + 1):
            dp.append([False] * (W + 1))
            dp[i][0] = True
        
        # dp数组的含义
        # 对于前i个数字，能否找到一个组合，使得其和为W
        # dp[N][W]表示对于所有的数字，能否找到加起来为W的组合
        # dp[N][0] = True, 表示所有的0，都可以找到一个空组合，使得加起来为0
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                # 是否要加入第i个数字
                if j - nums[i - 1] < 0:
                    # 不加入，加入了就超出了
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i - 1]]
        
        return dp[N][W]

# @lc code=end

