#
# @lc app=LeetCode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        
        if fast == None:
            return head.next
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        

        slow.next = slow.next.next
        return head
# @lc code=end

