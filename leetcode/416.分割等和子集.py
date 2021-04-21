#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all_nums = sum(nums)
        if all_nums % 2 == 1:
            return False
        target = all_nums // 2
        
        dp = []
        for i in range(len(nums) + 1):
            dp.append([False] * (target + 1))

        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
        return dp[len(nums)][target]
        

# @lc code=end

