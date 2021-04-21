#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        self.to_delete = to_delete
        root = self.helper(root)
        if root:
            self.res.append(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return root
        root.left = self.helper(root.left)
        root.right = self.helper(root.right)
        if root.val in self.to_delete:
            if root.left:
                self.res.append(root.left)
            if root.right:
                self.res.append(root.right)
            root = None
        return root

        
# @lc code=end

