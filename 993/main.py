# 993. 二叉树的堂兄弟节点
#
# 20200801
# huao
# 找从根结点到两个节点的路径
# 堂兄弟节点的要求为
#   1. 路径长相等
#   2. 路径中的倒数第二个节点不同
#   3. 为保证条件2，需要路径长度大于2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xRoute = self.getRoute(root, x)
        yRoute = self.getRoute(root, y)
        if len(xRoute) == len(yRoute) and len(xRoute) > 2 and xRoute[len(xRoute)-2] != yRoute[len(yRoute)-2]:
            return True
        else:
            return False

    def getRoute(self, root: TreeNode, num: int) -> List[TreeNode]:
        if root.val == num:
            return [root]
        if root.left != None:
            leftRoute = self.getRoute(root.left, num)
            if leftRoute != []:
                return [root] + leftRoute
        if root.right != None:
            rightRoute = self.getRoute(root.right, num)
            if rightRoute != []:
                return [root] + rightRoute
        return []
