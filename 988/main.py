# 988. 从叶结点开始的最小字符串
#
# 20200730
# huao
# 深度优先搜索一波，在最底层比较，把最小值返回来

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root: TreeNode, s='') -> str:
        if root == None:
            return s
        c = chr(root.val + 97)
        left = self.smallestFromLeaf(root.left, c+s)
        right = self.smallestFromLeaf(root.right, c+s)
        if root.left == None:
            return right
        elif root.right == None:
            return left
        else:
            return min(left, right)
        # if left == '':
        #     return right
        # elif right == '':
        #     return left
        # elif (left + c) < (right + c):
        #     return left + c
        # else:
        #     return right + c


sol = Solution()
root = TreeNode(4)
node1 = TreeNode(0)
node2 = TreeNode(1)
node3 = TreeNode(1)
root.left = node1
root.right = node2
node1.left = node3


print(sol.smallestFromLeaf(root))
