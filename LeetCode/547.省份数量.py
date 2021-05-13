#
# @lc app=LeetCode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0

        self.grid = isConnected

        n = len(isConnected)
        self.visited = [False] * n

        for i in range(n):
            if self.visited[i] == False:
                self.dfs(i)
                count += 1
        return count
    
    def dfs(self, i):
        self.visited[i] = True
        for j in range(len(self.grid[i])):
            if self.grid[i][j] == 1 and self.visited[j] == False:
                self.dfs(j)
        
# @lc code=end

