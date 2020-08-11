# 1008. 先序遍历构造二叉树
#
# 20200811
# huao
# 其实就是根据先序和中序构造二叉树
# 中序就是排序后的结果

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        length = len(preorder)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        midIndex = length
        for i in range(1, length):
            if preorder[i] > preorder[0]:
                midIndex = i
                break

        root.left = self.bstFromPreorder(preorder[1:midIndex])
        root.right = self.bstFromPreorder(preorder[midIndex:])
        return root
