# 563. 二叉树的坡度
#
# 20200809
# huao


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        return self.cal(root)[1]

    def cal(self, root: TreeNode):
        if root == None:
            return (0, 0)
        leftSum, leftTiltSum = self.cal(root.left)
        rightSum, rightTiltSum = self.cal(root.right)
        tiltSum = 0
        if leftSum > rightSum:
            tiltSum = leftSum - rightSum
        else:
            tiltSum = rightSum - leftSum
        return (leftSum + rightSum + root.val, leftTiltSum + rightTiltSum + tiltSum)
