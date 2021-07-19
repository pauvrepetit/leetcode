# 101. 对称二叉树
#
# 20210719
# huao

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymm(self, left: TreeNode, right: TreeNode) -> bool:
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self.isSymm(left.left, right.right) and self.isSymm(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isSymm(root.left, root.right)
