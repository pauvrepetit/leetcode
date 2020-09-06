# 107. 二叉树的层次遍历 II
#
# 20200906
# huao

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        order = [[root]]
        while True:
            nextLevel = []
            for node in order[-1]:
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
            if nextLevel != []:
                order.append(nextLevel)
            else:
                break
        valOrder = []
        for level in order[::-1]:
            vals = []
            for node in level:
                vals.append(node.val)
            valOrder.append(vals)
        return valOrder



