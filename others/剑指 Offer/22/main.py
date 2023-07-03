class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        count = 0
        original_head = head
        while head != None:
            count += 1
            head = head.next
        for i in range(count - k):
            original_head = original_head.next
        return original_head