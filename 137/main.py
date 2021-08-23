# 137. 只出现一次的数字 II
#
# 20210730
# huao
# 这个题线性复杂度我是没办法了

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 3
        return nums[-1]
