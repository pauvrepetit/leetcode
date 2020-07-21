# 24. 两两交换链表中的节点
#
# 20200721
# huao
# 指针指来指去而已

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        first = head.next
        second = head
        head = first
        tempLink = first.next
        first.next = second
        second.next = tempLink

        while second.next != None and second.next.next != None:
            tempHead = second
            first = second.next.next
            second = second.next
            tempHead.next = first
            tempLink = first.next
            first.next = second
            second.next = tempLink

        return head
