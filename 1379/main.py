# 1379. 找出克隆二叉树中的相同节点
#
# 20200802
# huao
# 这个如果没有值相同的节点的话 原树是不需要的
# 如果存在值相同的节点 那么需要在原树中找到该节点并保存其遍历路径(每一步的L or R)
# 然后在克隆树中按照相同的方法遍历一遍

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.findTarget(cloned, target.val)

    def findTarget(self, root: TreeNode, target: int) -> TreeNode:
        if root == None:
            return None
        elif root.val == target:
            return root
        else:
            leftNode = self.findTarget(root.left, target)
            if leftNode != None:
                return leftNode
            rightNode = self.findTarget(root.right, target)
            return rightNode
