# 105. 从前序与中序遍历序列构造二叉树
# 剑指 Offer 07. 重建二叉树
#
# 20200725
# huao
# 根据二叉树的前序和中序遍历构建二叉树
# 就是一个简单的递归调用而已

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        rootNode = TreeNode(preorder[0])
        splitLoc = inorder.index(preorder[0])
        rootNode.left = self.buildTree(preorder[1:splitLoc+1], inorder[:splitLoc])
        rootNode.right = self.buildTree(preorder[splitLoc+1:], inorder[splitLoc+1:])
        return rootNode


sol = Solution()
root = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
