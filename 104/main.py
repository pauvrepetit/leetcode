# 104. 二叉树的最大深度
# 剑指 Offer 55 - I. 二叉树的深度
#
# 20200725
# huao
# 递归而已

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
