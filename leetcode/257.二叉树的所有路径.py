#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        def preorder(root, track):
            if root == None:
                return

            if root.left == None and root.right == None:
                track.append(root.val)
                self.res.append('->'.join(str(node) for node in track))
                track.pop()
                return
            # 遍历
            track.append(root.val)
            preorder(root.left, track)
            preorder(root.right, track)
            track.pop()

        preorder(root, [])
        return self.res


# @lc code=end

