# 35. 搜索插入位置
#
# 20200724
# huao
# 有序数组 二分查找 仅此而已

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums))

    def binarySearch(self, nums: List[int], target: int, begin: int, end: int) -> int:
        if begin == end:
            return begin
        elif begin + 1 == end:
            if nums[begin] >= target:
                return begin
            else:
                return end

        mid = (begin + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, end)
        else:
            return self.binarySearch(nums, target, begin, mid)


sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 0))
