#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import List

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count_zero = 0
        index = 0
        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                nums[index] = num
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0

# @lc code=end

