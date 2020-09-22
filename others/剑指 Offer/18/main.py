# 剑指 Offer 18. 删除链表的节点
#
# 20200802
# huao
# 扫一遍 删节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        originHead = head
        while head.next != None:
            if head.next.val == val:
                head.next = head.next.next
                break
            else:
                head = head.next
        return originHead
