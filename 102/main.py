# 102. 二叉树的层序遍历
#
# 20200801
# huao
# 按层遍历 每一层放在一个单独的list中
# 那么下一个list中的元素就全部是上一个list的孩子

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        nodeList = [[root]]
        i = 0
        while True:
            levelNodeList = []
            for node in nodeList[len(nodeList)-1]:
                if node.left != None:
                    levelNodeList.append(node.left)
                if node.right != None:
                    levelNodeList.append(node.right)
            if levelNodeList == []:
                break
            nodeList.append(levelNodeList)
        for levelNodeList in nodeList:
            for i in range(len(levelNodeList)):
                levelNodeList[i] = levelNodeList[i].val
        return nodeList
