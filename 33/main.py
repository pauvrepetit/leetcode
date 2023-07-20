#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List
from bisect import bisect_left

# @lc code=start
class Solution:
    def sear(self, nums: List[int], target: int, begin: int, end: int) -> int:
        mid = (begin + end) // 2
        begin_val = nums[begin]
        mid_val = nums[mid]
        end_val = nums[end-1]
        if mid_val == target:
            return mid
        if begin_val == target:
            return begin
        if end_val == target:
            return end-1
        if begin == mid:
            return -1
        if begin_val < mid_val and target > begin_val and target < mid_val:
            index = bisect_left(nums, target, begin, mid)
            if index == mid or nums[index] != target:
                return -1
            return index
        if begin_val < mid_val:
            return self.sear(nums, target, mid, end)
        if target > mid_val and target < end_val:
            index = bisect_left(nums, target, mid, end)
            if index == end or nums[index] != target:
                return -1
            return index
        return self.sear(nums, target, begin, mid)

    def search(self, nums: List[int], target: int) -> int:
        return self.sear(nums, target, 0, len(nums))

# @lc code=end

print(Solution().search([1,3], 2))
