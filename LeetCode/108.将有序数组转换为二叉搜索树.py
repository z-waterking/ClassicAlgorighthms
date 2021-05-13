#
# @lc app=LeetCode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 直接从中间对其进行构造即可
        def bst(nums, start, end):
            if start > end:
                return None

            mid = start + (end - start) // 2
            root = TreeNode()
            root.val = nums[mid]

            root.left = bst(nums, start, mid - 1)
            root.right = bst(nums, mid + 1, end)
            return root

        root = bst(nums, 0, len(nums) - 1)
        return root
# @lc code=end

