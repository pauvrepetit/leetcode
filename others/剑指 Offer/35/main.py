
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mapping = dict()
        mapping[None] = None
        original_head = head
        while head != None:
            new_head = Node(head.val)
            mapping[head] = new_head
            head = head.next
        for head in mapping.keys():
            if head == None:
                continue
            new_head = mapping[head]
            new_head.next = mapping[head.next]
            new_head.random = mapping[head.random]
        return mapping[original_head]