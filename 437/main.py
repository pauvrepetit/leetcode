# 437. 路径总和 III
#
# 20200809
# huao
# 怎么对问题进行拆分 也是个问题

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None and sum == 0:
            return 0
        elif root == None:
            return 0
        return self.cal(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def cal(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        elif root.val == sum:
            return 1 + self.cal(root.left, 0) + self.cal(root.right, 0)
        else:
            return self.cal(root.left, sum - root.val) + self.cal(root.right, sum - root.val)


sol = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.right = node2
node2.right = node3
node3.right = node4
node4.right = node5

print(sol.pathSum(node1, 3))
