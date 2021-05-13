#
# @lc app=LeetCode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        return self.helper(root.left, root.right)

    def helper(self, l, r):
        if l == None and r == None:
            return True
        if l != None and r != None and l.val == r.val:
            return self.helper(l.left, r.right) and self.helper(l.right, r.left)
        return False
# @lc code=end

