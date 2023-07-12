class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSym(self, left: TreeNode, right: TreeNode) -> bool:
        if left == None and right == None:
            return True
        if left != None and right != None:
            if left.val != right.val:
                return False
            return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)
        return False


    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isSym(root.left, root.right)
            