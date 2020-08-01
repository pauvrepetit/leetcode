# 606. 根据二叉树创建字符串
#
# 20200801
# huao
# 递归

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t == None:
            return ""
        if t.left == None:
            if t.right == None:
                return str(t.val)
            else:
                return str(t.val) + "()(" + self.tree2str(t.right) + ")"
        else:
            if t.right == None:
                return str(t.val) + "(" + self.tree2str(t.left) + ")"
            else:
                return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"

