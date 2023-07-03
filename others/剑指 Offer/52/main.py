class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        original_headA = headA
        original_headB = headB
        lenA = 0
        lenB = 0
        while headA != None:
            headA = headA.next
            lenA += 1
        while headB != None:
            headB = headB.next
            lenB += 1
        if lenA > lenB:
            for _ in range(lenA - lenB):
                original_headA = original_headA.next
        else:
            for _ in range(lenB - lenA):
                original_headB = original_headB.next
        while True:
            if original_headA == original_headB:
                return original_headA
            original_headA = original_headA.next
            original_headB = original_headB.next
