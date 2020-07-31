# xh-2.6. 乘积最大子序列
#
# 20200731
# huao
# 取2的对数，结果就变成了找和最大的子序列
# 这就是算导上分治法的例题了

from typing import List
from math import log2


class Solution:
    def maxProductII(self, nums: List[float]) -> float:
        numsLog = []
        for num in nums:
            numsLog.append(int(log2(num)))
        return float(2 ** self.maxSubSum(numsLog, 0, len(numsLog)))

    def maxSubSum(self, nums: List[int], begin: int, end: int) -> int:
        if begin + 1 == end:
            return nums[begin]
        mid = (begin + end) // 2
        leftMax = self.maxSubSum(nums, begin, mid)
        rightMax = self.maxSubSum(nums, mid, end)

        leftEndMax = nums[mid - 1]
        nowSum = 0
        for i in range(begin, mid)[::-1]:
            nowSum += nums[i]
            leftEndMax = max(leftEndMax, nowSum)

        rightEndMax = nums[mid]
        nowSum = 0
        for i in range(mid, end):
            nowSum += nums[i]
            rightEndMax = max(rightEndMax, nowSum)

        return max(leftMax, rightMax, leftEndMax + rightEndMax)


sol = Solution()
print(sol.maxProductII([0.5, 0.5, 0.5]))
