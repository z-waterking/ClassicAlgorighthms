#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.res = []
        self.sub = {}
        
        self.helper(root)

        return self.res
    
    def helper(self, root):
        if root == None:
            return '#'

        left = self.helper(root.left)
        right = self.helper(root.right)

        subTree = left + ',' + right + ',' + str(root.val)


        if subTree not in self.sub:
            self.sub[subTree] = 1
        else:
            if self.sub[subTree] == 1:
                self.res.append(root)
            self.sub[subTree] += 1

        
        return subTree


# @lc code=end

