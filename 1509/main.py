# 1509. 三次操作后最大值与最小值的最小差
#
# 20200811
# huao

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        if length <= 4:
            return 0
        else:
            return min(nums[length-1]-nums[3], nums[length-2]-nums[2], nums[length-3]-nums[1], nums[length-4]-nums[0])
