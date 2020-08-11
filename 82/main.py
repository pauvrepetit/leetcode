# 82. 删除排序链表中的重复元素 II
#
# 20200811
# huao

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        noneHead = ListNode(-1)
        noneHead.next = head
        tempHead = noneHead

        while tempHead != None and tempHead.next != None and tempHead.next.next != None:
            if tempHead.next.val == tempHead.next.next.val:
                val = tempHead.next.val
                while tempHead.next != None and tempHead.next.val == val:
                    tempHead.next = tempHead.next.next
            else:
                tempHead = tempHead.next
        return noneHead.next

