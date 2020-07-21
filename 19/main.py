# 19. 删除链表的倒数第N个节点
#
# 20200721
# huao
# 设置两个指针向前移
# 第二个指针较第一个指针晚n步出发

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        realHead = head
        delNode = head
        for i in range(n):
            head = head.next
        if head == None:
            return realHead.next
        while head.next != None:
            head = head.next
            delNode = delNode.next
        delNode.next = delNode.next.next
        return realHead
