# 637. 二叉树的层平均值
#
# 20200912
# huao

from typing import List


def getAvg(level):
    s = 0
    for node in level:
        s += node.val
    return s // len(level)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return []
        levels = [[root]]
        while True:
            newLevel = []
            for node in levels[-1]:
                if node.left != None:
                    newLevel.append(node.left)
                if node.right != None:
                    newLevel.append(node.right)
            if newLevel == []:
                break
            else:
                levels.append(newLevel)
        avgs = list(map(getAvg, levels))
        return avgs
