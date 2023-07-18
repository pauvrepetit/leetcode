#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
from typing import Optional

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self, root: Optional[TreeNode]):
        if root == None:
            return 0, 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        depth = max(left[1], right[1]) + 1
        dia = max(left[0], right[0], left[1] + right[1] + 1)
        return dia, depth


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)[1] - 1
        
# @lc code=end

a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
Solution().diameterOfBinaryTree(a)