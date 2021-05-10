#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#

# @lc code=start
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # 先找其中一个岛屿
        # 1. 将所有的结点加入一个队列
        # 2. 将所有的格子赋值为2
        self.grid = A
        self.queue = []
        self.d = [-1, 0, 1, 0, -1]
        flag = False
        for i in range(len(A)):
            if flag == True:
                break
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    self.dfs(i, j)
                    flag = True
                    break

        level = 0
        while len(self.queue) != 0:
            level += 1
            n = len(self.queue)

            for i in range(n):
                r, c = self.queue.pop(0)
                for k in range(4):
                    # 朝四个方向找一次
                    x = r + self.d[k]
                    y = c + self.d[k+1]

                    if x >= 0 and x < len(self.grid) and y >= 0 and y < len(self.grid[0]):
                        if self.grid[x][y] == 2:
                            continue

                        # 找到了另外一个岛屿
                        if self.grid[x][y] == 1:
                            return level
                        
                        self.queue.append((x, y))
                        self.grid[x][y] = 2
        return level

    def dfs(self, i, j):
        if i < 0 or j < 0 or i == len(self.grid) or j == len(self.grid[0]) or self.grid[i][j] == 2:
            return
        if self.grid[i][j] == 0:
            self.queue.append((i, j))
            return

        self.grid[i][j] = 2
        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)
            

# @lc code=end

