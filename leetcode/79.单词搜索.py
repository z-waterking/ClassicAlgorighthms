#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.res = False
        self.visited = []
        for i in range(m):
            self.visited.append([False] * n)

        for i in range(m):
            for j in range(n):
                # 从这个位置开始搜索
                self.backtrack(board, word, i, j, 0)
        
        return self.res
    
    def backtrack(self, board, word, i, j, pos):
        # 判断是否出界
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        # 判断是否已走过
        if self.res == True or self.visited[i][j] == True:
            return
        # 判断是否相等
        if board[i][j] != word[pos]:
            return
        # 如果已经找到了，修改标记，返回
        if pos == len(word) - 1:
            self.res = True
            return
        # 回溯，标记为走过
        self.visited[i][j] = True
        # 检查周围四个位置
        self.backtrack(board, word, i+1, j, pos+1)
        self.backtrack(board, word, i-1, j, pos+1)
        self.backtrack(board, word, i, j+1, pos+1)
        self.backtrack(board, word, i, j-1, pos+1)
        # 撤销标记
        self.visited[i][j] = False
            
                
# @lc code=end

