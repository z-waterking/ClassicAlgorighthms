#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def helper(root):
            nonlocal res
            if root == None:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            res = max(res, l+r)
            return max(l, r) + 1
        helper(root)
        return res
# @lc code=end

