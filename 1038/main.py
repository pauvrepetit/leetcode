# 1038. 从二叉搜索树到更大和树
#
# 20200920
# huao

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sol(root, 0)
        return root
    
    def sol(self, root: TreeNode, s: int) -> int:
        if root == None:
            return s
        rightSum = self.sol(root.right, s)
        root.val += rightSum
        leftSum = self.sol(root.left, root.val)
        return leftSum