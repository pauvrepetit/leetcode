# 面试题 04.02. 最小高度树
#
# 20200730
# huao
# 就二分就行了

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        numsLen = len(nums)
        if numsLen == 0:
            return None
        root = TreeNode(nums[numsLen // 2])
        root.left = self.sortedArrayToBST(nums[: numsLen // 2])
        root.right = self.sortedArrayToBST(nums[numsLen // 2 + 1:])
        return root
