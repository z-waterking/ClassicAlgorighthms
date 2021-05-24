#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head):
            # 递归翻转链表
            if head == None or head.next == None:
                return head
            
            # 返回翻转后的表头
            p = reverse(head.next)

            head.next.next = head
            head.next = None

            return p

        return reverse(head)
# @lc code=end

