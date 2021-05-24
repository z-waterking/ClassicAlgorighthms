#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB

        while l1 != l2:
            if l1 != None:
                l1 = l1.next
            else:
                l1 = headB
            
            if l2 != None:
                l2 = l2.next
            else:
                l2 = headA
        
        return l1
        
# @lc code=end

