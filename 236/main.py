# 236. 二叉树的最近公共祖先
# 剑指 Offer 68 - II. 二叉树的最近公共祖先
#
# 20200801
# huao
# 这个算是235题的一个修改吧 235题是二叉搜索树 这个题是普通的二叉树
# 整体的做法是类似的
# 只不过这里要找到那个节点 需要做深度优先遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pRoute = self.getRoute(root, p.val)
        qRoute = self.getRoute(root, q.val)
        pLen = len(pRoute)
        qLen = len(qRoute)
        for i in range(min(pLen, qLen)):
            if pRoute[i] != qRoute[i]:
                return pRoute[i-1]
        if pLen > qLen:
            return qRoute[qLen-1]
        else:
            return pRoute[pLen-1]

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
