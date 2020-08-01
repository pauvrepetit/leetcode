# 110. 平衡二叉树
#
# 20200801
# huao
# 求以每个节点为根的子树的深度
# 根据定义
#       一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1
# 递归判断

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.setDepth(root)
        return self.check(root)

    def setDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        root.val = max(self.setDepth(root.left), self.setDepth(root.right)) + 1
        return root.val

    def check(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left != None and root.right != None:
            if root.left.val - root.right.val <= 1 and root.left.val - root.right.val >= -1:
                return self.check(root.left) and self.check(root.right)
            else:
                return False
        elif root.left == None and root.right == None:
            return True
        elif root.left != None and root.right == None:
            if root.left.val == 1:
                return True
            else:
                return False
        else:
            if root.right.val == 1:
                return True
            else:
                return False


sol = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node2.left = node1
node2.right = node4
node4.left = node3
node4.right = node5
node5.right = node6

print(sol.isBalanced(node2))
