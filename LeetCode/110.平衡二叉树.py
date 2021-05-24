#
# @lc app=LeetCode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res = self.helper(root)
        if res == -1:
            return False
        return True
        
    
    def helper(self, root):
        if root == None:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        # 如果已经不平衡了，返回-1
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        # 返回最大子数深度
        return 1 + max(left, right)
# @lc code=end

