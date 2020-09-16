# 462. 最少移动次数使数组元素相等 II
#
# 20200916
# huao
# 是中位数，不是平均数哦

from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        move = 0
        for num in nums:
            move += abs(num - mid)
        return move