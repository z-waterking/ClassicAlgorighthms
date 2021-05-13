#
# @lc app=LeetCode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        
        if root.val == key:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            
            temp = root.right
            while temp.left != None:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
        
# @lc code=end

