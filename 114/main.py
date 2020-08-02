# 114. 二叉树展开为链表
#
# 20200802
# huao
# 右子树移到左子树的右子树的右子树...的右子树上
# 左子树移到右子树的位置
# 递归

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        if root.left == None:
            self.flatten(root.right)
            return
        else:
            leftNode = root.left
            while leftNode.right != None:
                leftNode = leftNode.right
            leftNode.right = root.right
            root.right = root.left
            root.left = None
            self.flatten(root.right)
            return
