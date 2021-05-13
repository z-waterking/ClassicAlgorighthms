#
# @lc app=LeetCode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.track = ''
        self.res = []
        def helper(left, right):
            if left > right:
                return
            if left < 0 or right < 0:
                return
            
            if left == 0 and right == 0:
                self.res.append(self.track)
            
            self.track += '('
            helper(left-1, right)
            self.track = self.track[:-1]

            self.track += ')'
            helper(left, right - 1)
            self.track = self.track[:-1]

        helper(n, n)
        return self.res
# @lc code=end

