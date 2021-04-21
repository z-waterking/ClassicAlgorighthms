#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        q = [root]
        while len(q) != 0:
            num = len(q)
            s = 0
            for i in range(num):
                r = q[0]
                s += r.val
                q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            res.append(s / num)
        return res


# @lc code=end

