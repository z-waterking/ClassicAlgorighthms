#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 去对grid进行遍历，当发现一个1的时候，起码是1
        # 接着对周围进行探测，来更改一路走过的它的大小
        # 将所有的格子进行初始化，放入dp数组中
        self.d = [-1, 0, 1, 0, -1]
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
    
    def dfs(self, grid, i, j):
        
        if grid[i][j] == 0:
            return 0
        area = 1
        grid[i][j] = 0

        for k in range(len(self.d) - 1):
            x = i + self.d[k]
            y = j + self.d[k+1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                area += self.dfs(grid, x, y)

        return area

# @lc code=end

