# 106. 从中序与后序遍历序列构造二叉树
#
# 20210719
# huao

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        in_mid = inorder.index(root.val)
        root.left = self.buildTree(inorder[:in_mid], postorder[:in_mid])
        root.right = self.buildTree(inorder[in_mid+1:], postorder[in_mid:-1])
        return root


Solution().buildTree([1, 2, 3], [3, 2, 1])
