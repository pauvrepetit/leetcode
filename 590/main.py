# 590. N叉树的后序遍历
#
# 20200728
# huao
# 树的后序遍历

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        childs = []
        for child in root.children:
            childs += self.postorder(child)
        childs += [root.val]
        return childs
