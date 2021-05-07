#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = []
        queue = [root]

        flag = True

        while len(queue) != 0:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            if flag == True:
                flag = False
            else:
                flag = True
                temp.reverse()

            res.append(temp)
        return res
# @lc code=end

