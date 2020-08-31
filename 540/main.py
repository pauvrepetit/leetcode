# 540. 有序数组中的单一元素
#
# 20200831
# huao
# 无非就是分治法，就是特殊情况需要单独考虑一下

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return nums[self.cal(nums, 0, len(nums))]

    def cal(self, nums: List[int], begin: int, end: int) -> int:
        if begin == end - 1 or begin == end:
            return begin
        mid = (begin + end) // 2
        if mid == len(nums) - 1 or mid == 0:
            return mid
        if mid % 2 == 0:
            if nums[mid] == nums[mid+1]:
                return self.cal(nums, mid, end)
            elif nums[mid] == nums[mid-1]:
                return self.cal(nums, begin, mid)
            else:
                return mid
        else:
            if nums[mid] == nums[mid-1]:
                return self.cal(nums, mid, end)
            elif nums[mid] == nums[mid+1]:
                return self.cal(nums, begin, mid)
            else:
                return mid


print(Solution().singleNonDuplicate([2, 3, 3, 4, 4, 8, 8]))
print(Solution().singleNonDuplicate([3, 3, 7, 7, 10]))
