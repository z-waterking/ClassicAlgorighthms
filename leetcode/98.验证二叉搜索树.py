#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, min_root, max_root):
            if root == None:
                return True
            
            if min_root != None and root.val <= min_root.val:
                return False
            if max_root != None and root.val >= max_root.val:
                return False

            l = helper(root.left, min_root, root)
            r = helper(root.right, root, max_root)
            return l and r
        
        
        res = helper(root, None, None)
        return res
        
# @lc code=end

