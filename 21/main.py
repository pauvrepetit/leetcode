# 21. 合并两个有序链表
#
# 20200721
# huao
# 简单的数据结构题


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergeListBegin = ListNode()
        mergeList = mergeListBegin
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                mergeList.next = l1
                mergeList = mergeList.next
                l1 = l1.next
            else:
                mergeList.next = l2
                mergeList = mergeList.next
                l2 = l2.next
        if l1 != None:
            mergeList.next = l1
        else:
            mergeList.next = l2
        return mergeListBegin.next


sol = Solution()
