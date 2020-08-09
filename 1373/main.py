# 1373. 二叉搜索子树的最大键值和
#
# 20200809
# huao
# CSP不能马上看结果来修改是真的难...

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        maxSum, _, _ = self.sol(root)
        return maxSum

    def sol(self, root: TreeNode):
        if root == None:
            return (0, 0, True)
        left, allLeft, leftIsBST = self.sol(root.left)
        right, allRight, rightIsBST = self.sol(root.right)
        if leftIsBST and rightIsBST:
            if self.checkBST(root):
                return (max(left, right, allLeft + allRight + root.val), allLeft + allRight + root.val, True)
            else:
                return (max(left, right), 0, False)
        else:
            return (max(left, right), 0, False)

    def checkBST(self, root: TreeNode) -> bool:
        leftMax = 0
        rightMin = 0
        if root.left != None:
            node = root.left
            while node.right != None:
                node = node.right
            leftMax = node.val
        else:
            leftMax = root.val - 1

        if root.right != None:
            node = root.right
            while node.left != None:
                node = node.left
            rightMin = node.val
        else:
            rightMin = root.val + 1
        return (leftMax < root.val and rightMin > root.val)
