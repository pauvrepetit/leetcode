# 160. 相交链表
#
# 20210730
# huao
# 人有点呆了，看来今天不是很适合做题

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        beginA = headA
        lastA = None
        lenA = 0
        while beginA != None:
            lenA += 1
            lastA = beginA
            beginA = beginA.next

        beginB = headB
        lastB = None
        lenB = 0
        while beginB != None:
            lenB += 1
            lastB = beginB
            beginB = beginB.next

        if lastA != lastB:
            return None

        beginA = headA
        beginB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                beginA = beginA.next
        else:
            for i in range(lenB - lenA):
                beginB = beginB.next
        while beginA != beginB:
            beginA = beginA.next
            beginB = beginB.next
        return beginA
