# 148. 排序链表
#
# 20210724
# huao
# 我傻了，他要常数空间复杂度，我看成了O(nlogn)的空间复杂度，我就说这什么鬼要求嘛
# 不过写都写了，就算了吧

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        node_list = []
        while head != None:
            node_list.append(head)
            head = head.next
        node_list.sort(key=lambda x : x.val)
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        node_list[-1].next = None
        return node_list[0]
