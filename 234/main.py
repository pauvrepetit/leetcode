#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPal(self, head: Optional[ListNode], length: int):
        if head == None:
            return True, None
        if length == 0:
            return True, head
        if length == 1:
            return True, head.next
        pal, next = self.isPal(head.next, length-2)
        if not pal:
            return False, None
        if head.val == next.val:
            return True, next.next
        return False, None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        node = head
        while node != None:
            length += 1
            node = node.next
        return self.isPal(head, length)[0]

# @lc code=end

Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
