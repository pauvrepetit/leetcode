# 面试题 02.04. 分割链表
#
# 20200726
# huao
# 扫一遍链表，比较一下

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessNode = None
        greatNode = None
        originNode = head
        while originNode != None:
            if originNode.val < x:
                newNode = ListNode(originNode.val)
                newNode.next = lessNode
                lessNode = newNode
            else:
                newNode = ListNode(originNode.val)
                newNode.next = greatNode
                greatNode = newNode
            originNode = originNode.next
        originNode = lessNode
        if originNode == None:
            return greatNode
        else:
            while originNode.next != None:
                originNode = originNode.next
            originNode.next = greatNode
            return lessNode
