#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
from typing import Optional

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        new_head = Node(head.val, None, head.random)
        node = head.next
        new_node = new_head
        mapping = dict()
        mapping[head] = new_head
        mapping[None] = None
        while node != None:
            new_node.next = Node(node.val, None, node.random)
            mapping[node] = new_node.next
            new_node = new_node.next
            node = node.next
        node = new_head
        while node != None:
            node.random = mapping[node.random]
            node = node.next
        return new_head
# @lc code=end

