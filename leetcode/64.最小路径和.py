#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
import copy
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = copy.deepcopy(grid)
        m = len(grid)
        n = len(grid[0])
        # init
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + dp[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + dp[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j] + dp[i][j], dp[i][j-1] + dp[i][j])
        
        return dp[m-1][n-1]
        

# @lc code=end

