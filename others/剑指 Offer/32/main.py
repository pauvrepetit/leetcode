# 剑指 Offer 32 - I. 从上到下打印二叉树
#
# 20200731
# huao
# 二叉树按层遍历
# 用一个队列就ok

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        queue = [root]
        i = 0
        while i < len(queue):
            if queue[i].left != None:
                queue.append(queue[i].left)
            if queue[i].right != None:
                queue.append(queue[i].right)
            i += 1
        numsQueue = []
        for node in queue:
            numsQueue.append(node.val)
        return numsQueue


root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
root.left = node1
root.right = node2
node3 = TreeNode(15)
node4 = TreeNode(7)
node2.left = node3
node2.right = node4
sol = Solution()
print(sol.levelOrder(root))
