class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        l = None
        if l1.val < l2.val:
            l = l1
            l1 = l1.next
        else:
            l = l2
            l2 = l2.next
        original_l = l
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
                l = l.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next
        if l1 == None:
            l.next = l2
        else:
            l.next = l1
        return original_l