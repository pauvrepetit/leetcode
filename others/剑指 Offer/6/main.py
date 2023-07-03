from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head == None:
            return []
        values = [head.val]
        while head.next != None:
            head = head.next
            values.append(head.val)
        values.reverse()
        return values
