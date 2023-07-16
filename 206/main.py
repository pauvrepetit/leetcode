#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rev(self, head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        next = head.next
        head.next = prev
        if next == None:
            return head
        return self.rev(next, head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rev(head, None)
        # if head == None or head.next == None:
        #     return head
        # return self.rev(head.next, head)
        
# @lc code=end

a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
Solution().reverseList(a)