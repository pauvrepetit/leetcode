class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def check(self, root: TreeNode):
        if root == None:
            return (True, 0)
        if root.left == None and root.right == None:
            return (True, 1)
        left = self.check(root.left)
        right = self.check(root.right)
        return (left[0] and right[0] and abs(left[1] - right[1]) <= 1, max(left[1], right[1]) + 1)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root)[0]