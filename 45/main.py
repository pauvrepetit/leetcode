#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 对于每个点，记录最前面那个能跳到这个点的点
        points = [i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, min(i + nums[i] + 1, len(nums))):
                points[j] = min(points[j], i)
        count = 0
        loc = len(nums) - 1
        while loc != 0:
            count += 1
            loc = points[loc]
        return count

# @lc code=end

