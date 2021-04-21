#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode()
        root.val = postorder[-1]

        in_index = inorder.index(root.val)
        
        left_postorder = postorder[0:in_index]
        right_postorder = postorder[in_index:-1]

        left_inorder = inorder[:in_index]
        right_inorder = inorder[in_index+1:]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
# @lc code=end

