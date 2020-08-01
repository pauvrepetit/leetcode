# 235. 二叉搜索树的最近公共祖先
# 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
#
# 20200801
# huao
# 找到由根结点开始到两个节点的路径
# 找两个路径的最长公共前缀
# 最长公共前缀的最后一个节点即为二者的最近公共祖先

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
        elif num > root.val:
            return [root] + self.getRoute(root.right, num)
        else:
            return [root] + self.getRoute(root.left, num)
