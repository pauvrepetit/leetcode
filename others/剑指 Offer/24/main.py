class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        next = None
        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev