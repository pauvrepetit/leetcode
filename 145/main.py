# 145. 二叉树的后序遍历
#
# 20200811
# huao
# 递归法自然是很好写的
# 改成迭代 其实也是一样
# 结果我写的迭代 还没有 递归 测试得快...

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归法
        # if root == None:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        # 迭代法
        if root == None:
            return []
        stack = [root]
        seeStack = [0]
        level = 0
        postorderList = []
        while stack != []:
            level = len(stack) - 1
            if stack[level] == None:
                stack.pop()
                seeStack.pop()
                continue
            if seeStack[level] == 0:
                seeStack[level] += 1
                stack.append(stack[level].left)
                seeStack.append(0)
                continue
            if seeStack[level] == 1:
                seeStack[level] += 1
                stack.append(stack[level].right)
                seeStack.append(0)
                continue
            if seeStack[level] == 2:
                postorderList.append(stack[level].val)
                stack.pop()
                seeStack.pop()
                continue
        return postorderList


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3
sol = Solution()
print(sol.postorderTraversal(node1))
