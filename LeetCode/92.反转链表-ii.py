#
# @lc app=LeetCode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)
        
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head
    
    def reverseN(self, head, n):
        if n == 1:
            self.succesor = head.next
            return head
        
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.succesor

        return last
# @lc code=end

