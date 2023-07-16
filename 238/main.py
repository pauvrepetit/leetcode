#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from typing import List

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        end_list = [1 for _ in nums]
        for i in range(len(end_list) - 1)[::-1]:
            end_list[i] = end_list[i+1] * nums[i+1]
        front = 1
        for i in range(1, len(nums)):
            front *= nums[i-1]
            end_list[i] *= front
        return end_list
# @lc code=end

