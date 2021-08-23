# 142. 环形链表 II
#
# 20210730
# huao
# 呜呜呜 我好蠢呀 月栋给我讲过那么多次的快慢指针 我还是不会写

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return None
        fast = head
        slow = head
        fast = fast.next.next
        slow = slow.next
        while fast != slow:
            if fast == None or fast.next == None:
                return None
            fast = fast.next.next
            slow = slow.next
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
