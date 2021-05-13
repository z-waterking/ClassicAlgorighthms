#
# @lc app=LeetCode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        self.rank = 0
        def helper(root, k):
            if root == None:
                return
            helper(root.left, k)
            self.rank += 1
            if self.rank == k:
                self.res = root.val
            helper(root.right, k)
        
        helper(root, k)
        return self.res
# @lc code=end

