# 141. 环形链表
#
# 20200729
# huao
# 判链表是否有环，看似简单，但是写出来还是O(n^2)
# 大概是需要一个更复杂的数据结构来描述已经扫描过的节点，可以降低查找的复杂度吧

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodeList = []
        while head != None:
            if head.next in nodeList:
                return True
            else:
                nodeList.append(head.next)
                head = head.next
        return False
