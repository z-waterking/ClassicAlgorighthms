#
# @lc app=LeetCode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode()
        root.val = preorder[0]

        in_index = inorder.index(root.val)
        
        left_preorder = preorder[1:in_index+1]
        right_preorder = preorder[in_index+1:]

        left_inorder = inorder[:in_index]
        right_inorder = inorder[in_index+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
# @lc code=end

