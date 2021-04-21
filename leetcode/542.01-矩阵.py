#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        res = []
        for i in range(m):
            res.append([m*n] * n)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i-1][j] + 1, res[i][j])
                    if j > 0:
                        res[i][j] = min(res[i][j-1] + 1, res[i][j])
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i < m-1:
                        res[i][j] = min(res[i+1][j] + 1, res[i][j])
                    if j < n-1:
                        res[i][j] = min(res[i][j+1] + 1, res[i][j])
        
        return res
                    
# @lc code=end

