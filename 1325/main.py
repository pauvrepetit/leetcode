# 1325. 删除给定值的叶子节点
#
# 20200810
# huao
# 递归啊递归

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root == None:
            return root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left == None and root.right == None and root.val == target:
            return None
        else:
            return root
