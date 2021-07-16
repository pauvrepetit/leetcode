# 61. 旋转链表
#
# 20210716
# huao


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        list_len = 1
        n = head
        while n.next != None:
            list_len += 1
            n = n.next
        n.next = head

        k = list_len - k % list_len
        n = head
        for i in range(k - 1):
            n = n.next
        head = n.next
        n.next = None
        return head
