# 669. 修剪二叉搜索树
#
# 20200802
# huao
# 以修剪小元素为例
# 如果根结点等于L，则将其左子树置为None
# 如果大于L，那么对其左子树递归
# 如果小于L，那么根结点也要剪去，对其右子树递归
# 修剪大元素 类似

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        return self.trimBSTRight(self.trimBSTLeft(root, L), R)

    def trimBSTLeft(self, root: TreeNode, L: int) -> TreeNode:
        if root == None:
            return None
        if root.val == L:
            root.left = None
            return root
        elif root.val < L:
            return self.trimBSTLeft(root.right, L)
        else:
            root.left = self.trimBSTLeft(root.left, L)
            return root

    def trimBSTRight(self, root: TreeNode, R: int) -> TreeNode:
        if root == None:
            return None
        if root.val == R:
            root.right = None
            return root
        elif root.val > R:
            return self.trimBSTRight(root.left, R)
        else:
            root.right = self.trimBSTRight(root.right, R)
            return root
