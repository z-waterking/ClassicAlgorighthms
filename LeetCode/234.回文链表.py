#
# @lc app=LeetCode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        return self.reverse(head)
    
    def reverse(self, right):
        if right == None:
            return True
        
        res = self.reverse(right.next)
        res = res and (self.left.val == right.val)
        self.left = self.left.next
        return res
# @lc code=end

