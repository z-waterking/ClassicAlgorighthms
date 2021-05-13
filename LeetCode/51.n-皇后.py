#
# @lc app=LeetCode.cn id=51 lang=python3
#
# [51] N 皇后
#
import copy
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []

        self.board = []
        for i in range(n):
            self.board.append("." * n)
        
        self.backtrack(self.board, 0)
        return self.res
    
    def backtrack(self, board, row):
        if row == len(board):
            self.res.append(copy.deepcopy(board))
            return
        
        for col in range(len(board[row])):
            if self.isValid(board, row, col) == False:
                continue
            # 放一个Q
            temp = list(board[row])
            temp[col] = 'Q'
            board[row] = ''.join(temp)

            self.backtrack(board, row + 1)
            # 撤销Q
            temp = list(board[row])
            temp[col] = '.'
            board[row] = ''.join(temp)

    
    def isValid(self, board, row, col):
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        i = row
        j = col
        while i >= 0 and j < len(board[0]):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
            
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        return True
# @lc code=end

