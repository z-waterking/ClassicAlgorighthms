#
# @lc app=LeetCode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root == None:
            return 0
            
        res = self.pathSumStartsWith(root, targetSum) + \
                self.pathSum(root.left, targetSum)+ \
                self.pathSum(root.right, targetSum)
        return res

    def pathSumStartsWith(self, root, targetSum):
        if root == None:
            return 0

        count = 0
        if root.val == targetSum:
            count = 1
        count += self.pathSumStartsWith(root.left, targetSum-root.val)
        count += self.pathSumStartsWith(root.right, targetSum-root.val)
        return count
        
# @lc code=end

