#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
from typing import Optional, List

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from queue import Queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        queue = Queue()
        queue.put([root, 0])
        res = []
        index = 0
        while not queue.empty():
            node, depth = queue.get()
            if index == depth:
                res.append(node.val)
                index += 1
            if node.right != None:
                queue.put([node.right, depth + 1])
            if node.left != None:
                queue.put([node.left, depth + 1])
        return res

# @lc code=end

