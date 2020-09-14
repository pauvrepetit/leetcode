# 94. 二叉树的中序遍历
#
# 20200914
# huao

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack = [[root, 0]]
        travel = []
        while stack != []:
            if stack[-1][1] == 0:
                stack[-1][1] += 1
                if stack[-1][0].left != None:
                    stack.append([stack[-1][0].left, 0])
            elif stack[-1][1] == 1:
                stack[-1][1] += 1
                travel.append(stack[-1][0].val)
            elif stack[-1][1] == 2:
                stack[-1][1] += 1
                if stack[-1][0].right != None:
                    stack.append([stack[-1][0].right, 0])
            else:
                stack.pop()
        return travel

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
node1.left = node2
print(Solution().inorderTraversal(root))