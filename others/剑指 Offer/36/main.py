
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def transfer(self, root: 'Node', next: 'Node') -> 'Node':
        if root == None:
            return next
        if root.left == None and root.right == None:
            root.right = next
            return root
        root.right = self.transfer(root.right, next)
        return self.transfer(root.left, root)


    def treeToDoublyList(self, root: 'Node') -> 'Node':
        begin = self.transfer(root, None)
        if begin == None:
            return None
        node = begin
        while node.right != None:
            node.right.left = node
            node = node.right
        node.right = begin
        begin.left = node
        return begin

# a = Node(1)
b = Node(2)
c = Node(3)
# d = Node(4)
# e = Node(5)

# d.left = b
# d.right = e
# b.left = a
# b.right = c
b.right = c

print(Solution().treeToDoublyList(b).val)