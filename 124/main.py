from typing import Optional, List

#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# 还是各种细节需要考虑
# 首先是叶子节点的问题
# 跨越root的路径可以不包含左边的路径/右边的路径，甚至可以只包含root节点

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.compute(root)[2]

    def compute(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return [-0xFFFFF, -0xFFFFF, -0xFFFFF]
        left = self.compute(root.left)
        right = self.compute(root.right)
        left_path = root.val + max(left[0], left[1], 0) if root.left != None else root.val
        right_path = root.val + max(right[0], right[1], 0) if root.right != None else root.val
        max_path = max(left[2], right[2], left_path + right_path - root.val, left_path, right_path, root.val)
        return [left_path, right_path, max_path]


# @lc code=end
