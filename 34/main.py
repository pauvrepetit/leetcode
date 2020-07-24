# 34. 在排序数组中查找元素的第一个和最后一个位置
#
# 20200724
# huao
# 有序数组 二分查找
# 找数组中的target第一次和最后一次出现的位置

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchLeft(nums, target, 0, len(nums)), self.searchRight(nums, target, 0, len(nums))]

    def searchLeft(self, nums: List[int], target: int, begin: int, end: int) -> List[int]:
        if begin == end:
            return -1
        elif begin + 1 == end and nums[begin] == target:
            return begin
        elif begin + 1 == end:
            return -1
        elif begin + 2 == end:
            if nums[begin] == target:
                return begin
            elif nums[begin + 1] == target:
                return begin + 1
            else:
                return -1

        mid = (begin + end) // 2
        if nums[mid] < target:
            return self.searchLeft(nums, target, mid, end)
        else:
            return self.searchLeft(nums, target, begin, mid + 1)

    def searchRight(self, nums: List[int], target: int, begin: int, end: int) -> List[int]:
        if begin == end:
            return -1
        elif begin + 1 == end and nums[begin] == target:
            return begin
        elif begin + 1 == end:
            return -1
        elif begin + 2 == end:
            if nums[begin + 1] == target:
                return begin + 1
            elif nums[begin] == target:
                return begin
            else:
                return -1

        mid = (begin + end) // 2
        if nums[mid] <= target:
            return self.searchRight(nums, target, mid, end)
        else:
            return self.searchRight(nums, target, begin, mid + 1)


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
