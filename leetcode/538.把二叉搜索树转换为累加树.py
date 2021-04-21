#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def helper(root):
            if root == None:
                return 

            helper(root.right)

            self.sum = self.sum + root.val
            root.val = self.sum

            helper(root.left)
        helper(root)
        return root
# @lc code=end

