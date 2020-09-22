# 面试题 02.03. 删除中间节点
#
# 20200811
# huao
# 单链表中删除一个中间节点(非首尾节点)
# 只给出了待删除的节点的指针
# emmm...
# 把下一个节点的值拷贝到这里来，然后把下一个节点删掉...

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

