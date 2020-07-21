# 95. 不同的二叉搜索树 II
#
# 20200721
# huao
#
# 递归而已

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        i = 0
        queue = [self]
        numQueue = [self.val]
        while i < len(queue):
            if queue[i] == None:
                i += 1
                continue
            if queue[i].left != None or queue[i].right != None:
                queue.append(queue[i].left)
                queue.append(queue[i].right)
                if queue[i].left != None:
                    numQueue.append(queue[i].left.val)
                else:
                    numQueue.append(None)
                if queue[i].right != None:
                    numQueue.append(queue[i].right.val)
                else:
                    numQueue.append(None)
                i += 1
            else:
                i += 1
        return str(numQueue)

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        trees = []
        for i in range(n):
            val = i + 1
            ltree = self.generateSubTrees(0, i)
            rtree = self.generateSubTrees(i + 1, n)
            for lt in ltree:
                for rt in rtree:
                    newTree = TreeNode(val, lt, rt)
                    trees.append(newTree)
        return trees


    def generateSubTrees(self, begin: int, end: int) -> List[TreeNode]:
        if begin == end:
            return [None]
        trees = []
        for i in range(end - begin):
            val = i + begin + 1
            ltree = self.generateSubTrees(begin, i + begin)
            rtree = self.generateSubTrees(i + begin + 1, end)
            for lt in ltree:
                for rt in rtree:
                    newTree = TreeNode(val, lt, rt)
                    trees.append(newTree)
        return trees


sol = Solution()
for tree in sol.generateTrees(3):
    print(tree)
