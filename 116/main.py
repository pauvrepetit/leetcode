# 116. 填充每个节点的下一个右侧节点指针
#
# 20210724
# huao

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None or root.left == None:
            return root
        root.left.next = root.right
        root.right.next = None if root.next == None else root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
