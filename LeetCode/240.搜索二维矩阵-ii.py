#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 每行每列都是递增的
        # 从右上角开始进行查找
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            # 如果target小,往小的方向找
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False


# @lc code=end

