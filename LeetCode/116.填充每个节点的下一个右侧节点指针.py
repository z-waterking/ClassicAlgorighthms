#
# @lc app=LeetCode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return
        root.next = None
        self.helper(root.left, root.right)
        return root
    
    def helper(self, left, right):
        if left == None or right == None:
            return
        left.next = right
        self.helper(left.left, left.right)
        self.helper(right.left, right.right)
        self.helper(left.right, right.left)
        
# @lc code=end

