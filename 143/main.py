# 143. 重排链表
#
# 20210730
# huao

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        node_list = []
        begin = head
        while begin != None:
            node_list.append(begin)
            begin = begin.next
        head = node_list[0]
        now_node = head
        for i in range(1, len(node_list)):
            if i % 2 == 1:
                now_node.next = node_list[-(i // 2)-1]
            else:
                now_node.next = node_list[i // 2]
            now_node = now_node.next
        now_node.next = None
