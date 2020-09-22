# 面试题 04.10. 检查子树
#
# 20200728
# huao
# 判断二叉树t2是不是t1的子树
# 很暴力的方法呀

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None:
            return False
        if t1.val == t2.val:
            sameTree = self.checkFullTree(t1, t2)
            if sameTree == True:
                return True
            else:
                return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
        else:
            return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def checkFullTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False

        if t1.val != t2.val:
            return False
        else:
            return self.checkFullTree(t1.left, t2.left) and self.checkFullTree(t1.right, t2.right)
