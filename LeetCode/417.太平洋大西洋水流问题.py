#
# @lc app=LeetCode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m = len(heights)
        n = len(heights[0])

        self.d = [-1, 0, 1, 0, -1]
        self.rea_p = []
        self.rea_a = []
        for i in range(m):
            self.rea_p.append([False] * n)
            self.rea_a.append([False] * n)
        
        # 倒着找能流到太平洋的位置
        for i in range(m):
            self.dfs(heights, i, 0, True)
        for j in range(n):
            self.dfs(heights, 0, j, True)

        # 倒着找能流到大西洋的位置
        for i in range(m):
            self.dfs(heights, i, n - 1, False)
        for j in range(n):
            self.dfs(heights, m - 1, j, False)

        # 判断哪些点可以
        for i in range(m):
            for j in range(n):
                if self.rea_p[i][j] == True and self.rea_a[i][j] == True:
                    res.append([i, j])

        return res

    def dfs(self, heights, i, j, isP):
        if isP == True:
            if self.rea_a[i][j] == True:
                return
            self.rea_a[i][j] = True
        else:
            if self.rea_p[i][j] == True:
                return
            self.rea_p[i][j] = True
        
        for k in range(4):
            x = i + self.d[k]
            y = j + self.d[k+1]
            if x >= 0 and x < len(heights)\
            and y >= 0 and y < len(heights[0])\
                and heights[i][j] <= heights[x][y]:
                self.dfs(heights, x, y, isP)

# @lc code=end

