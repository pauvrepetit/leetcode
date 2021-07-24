# 117. 填充每个节点的下一个右侧节点指针 II
#
# 20210724
# huao
# tmd 这个需要先递归右边，不然会出问题

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        if root.left == None and root.right == None:
            return root
        begin = root.next
        tmp_next = None
        while begin != None:
            if begin.left != None:
                tmp_next = begin.left
                break
            elif begin.right != None:
                tmp_next = begin.right
                break
            begin = begin.next
        if root.left == None:
            root.right.next = tmp_next
            self.connect(root.right)
        elif root.right == None:
            root.left.next = tmp_next
            self.connect(root.left)
        else:
            root.left.next = root.right
            root.right.next = tmp_next
            self.connect(root.right)
            self.connect(root.left)
        return root
