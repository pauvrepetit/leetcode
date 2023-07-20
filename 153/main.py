#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
from typing import List

# @lc code=start
class Solution:
    def find(self, nums: List[int], begin: int, end: int) -> int:
        mid = (begin + end) // 2
        begin_val = nums[begin]
        mid_val = nums[mid]
        end_val = nums[end-1]
        if begin_val < end_val:
            return begin_val
        if begin == mid or begin+2 == end:
            return mid_val
        if begin_val < mid_val:
            return self.find(nums, mid, end)
        return self.find(nums, begin, mid+1)

    def findMin(self, nums: List[int]) -> int:
        return self.find(nums, 0, len(nums))
# @lc code=end

print(Solution().findMin([2,3,1]))
