#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
from typing import List

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        tmp = nums[-k:]
        for i in range(len(nums) - k)[::-1]:
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = tmp[i]
# @lc code=end
