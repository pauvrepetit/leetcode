# 987. 二叉树的垂序遍历
#
# 20200917
# huao

from typing import List
from functools import cmp_to_key


def cmp(x, y):
    xx = x[1][0]
    xy = x[1][1]
    yx = y[1][0]
    yy = y[1][1]
    xnode = x[0].val
    ynode = y[0].val

    if xx < yx:
        return -1
    elif xx > yx:
        return 1
    else:
        if xy > yy:
            return -1
        elif xy < yy:
            return 1
        else:
            if xnode > ynode:
                return 1
            elif xnode == ynode:
                return 0
            else:
                return -1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        nodeList = []
        stack = [[root, [0, 0]]]
        while stack != []:
            node = stack.pop()
            nodeList.append(node)
            if node[0].left != None:
                stack.append([node[0].left, [node[1][0]-1, node[1][1]-1]])
            if node[0].right != None:
                stack.append([node[0].right, [node[1][0]+1, node[1][1]-1]])
        nodeList.sort(key=cmp_to_key(cmp))
        numList = {}
        for node, [x, y] in nodeList:
            if x in numList.keys():
                numList[x].append(node.val)
            else:
                numList[x] = [node.val]
        return numList.values()
