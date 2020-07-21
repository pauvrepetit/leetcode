# 23. 合并K个排序链表
#
# 20200721
# huao
# 排序 二分查找->插入
# 对链表组成的list按照链表首元素排序(n*log n)，这样每次取的就是第一个链表的第一个元素
# 取完该节点后，需要更新该链表的位置，用二分查找(log n)
# 下次继续取首链表的首节点

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while None in lists:
            lists.remove(None)
        lists.sort(key=lambda x: x.val)

        mergeListBegin = ListNode(0)
        mergeList = mergeListBegin
        while True:
            if len(lists) == 0:
                break
            else:
                mergeList.next = lists[0]
                lists[0] = lists[0].next
                mergeList = mergeList.next
                if lists[0] == None:
                    del lists[0]
                else:
                    self.resort(lists)
        return mergeListBegin.next

    def resort(self, lists: List[ListNode]) -> List[ListNode]:
        if len(lists) == 1:
            return lists
        list0 = lists.pop(0)
        lists.insert(self.binary_search(lists, 0, len(lists), list0.val), list0)
        return lists

    def binary_search(self, lists: List[ListNode], begin: int, end: int, target: int) -> int:
        mid = (begin + end) // 2
        if begin == end or begin + 1 == end:
            if lists[begin].val < target:
                return begin + 1
            else:
                return begin
        elif lists[mid].val < target:
            return self.binary_search(lists, mid, end, target)
        elif lists[mid].val > target:
            return self.binary_search(lists, begin, mid, target)
        else:
            return mid


sol = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(2)
l1.next = l2
l2.next = l3

l4 = ListNode(1)
l5 = ListNode(1)
l6 = ListNode(2)
l4.next = l5
l5.next = l6

# l7 = ListNode(2)
# l8 = ListNode(6)
# l7.next = l8

sol.mergeKLists([l1, l4])