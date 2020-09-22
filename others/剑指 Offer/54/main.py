# 剑指 Offer 54. 二叉搜索树的第k大节点
#
# 20200810
# huao
# 这...二叉搜索树 中序遍历就是有序的 再找第k大节点...
# 或者有些更好的方法吧

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        treeList = self.treeToList(root)
        return treeList[len(treeList)-k]

    def treeToList(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            return self.treeToList(root.left) + [root.val] + self.treeToList(root.right)
