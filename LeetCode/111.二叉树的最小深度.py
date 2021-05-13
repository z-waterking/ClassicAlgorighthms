#
# @lc app=LeetCode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [root]
        height = 1
        while len(queue) != 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return height
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height += 1
        return height


# @lc code=end

