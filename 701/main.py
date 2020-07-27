# 701. 二叉搜索树中的插入操作
#
# 20200727
# huao
# 直接通过递归的方法插入到二叉搜索树的叶子上面，这就是最简单的做法了吧
# 这样，虽然写起来简单，但是感觉不怎么好啊，这棵树不平衡，起不到二叉搜素树的作用...

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            newNode = TreeNode(val)
            return newNode
        if root.val < val:
            if root.right == None:
                newNode = TreeNode(val)
                root.right = newNode
            else:
                self.insertIntoBST(root.right, val)
        else:
            if root.left == None:
                newNode = TreeNode(val)
                root.left = newNode
            else:
                self.insertIntoBST(root.left, val)
        return root
