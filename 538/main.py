# 538. 把二叉搜索树转换为累加树
#
# 20200920
# huao

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sol(root, 0)
        return root
    
    def sol(self, root: TreeNode, s: int) -> int:
        if root == None:
            return s
        rightSum = self.sol(root.right, s)
        root.val += rightSum
        leftSum = self.sol(root.left, root.val)
        return leftSum