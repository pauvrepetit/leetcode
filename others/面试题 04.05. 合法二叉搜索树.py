# 面试题 04.05. 合法二叉搜索树
# 98. 验证二叉搜索树
#
# 20200801
# huao
# 二叉搜索树的特点：中序遍历的结果是绝对单调递增的(不存在相等的元素

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.getInOrder(root)
        for i in range(1, len(inorder)):
            if inorder[i - 1] >= inorder[i]:
                return False
        return True

    def getInOrder(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            return self.getInOrder(root.left) + [root.val] + self.getInOrder(root.right)
