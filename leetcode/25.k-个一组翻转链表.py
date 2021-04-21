#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return
        a = head
        b = head
        for i in range(k):
            if b == None:
                return head
            b = b.next
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead

    def reverse(self, head, tail):
        pre = None
        cur = head
        nxt = head

        while cur != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            
        return pre
# @lc code=end

