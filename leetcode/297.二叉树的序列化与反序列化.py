#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = ''
        def helper(root):
            if root == None:
                self.res = self.res + 'null' + ','
                return
            
            self.res = self.res + str(root.val) + ','
            helper(root.left)
            helper(root.right)

        helper(root)
        return self.res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data):
            v = self.data.pop(0)
            if v == 'null':
                return
            
            root = TreeNode(v)
            root.left = helper(self.data)
            root.right = helper(self.data)
            return root

        self.data = data.split(',')
        root = helper(self.data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

