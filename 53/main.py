# 53. 最大子序和
#
# 20210716
# huao
#
# 这是算导上分治法的例题

from typing import List


class Solution:
    def maxSub(self, nums: List[int], begin: int, end: int) -> int:
        if end - begin == 1:
            return nums[begin]
        mid = (begin + end) // 2
        left_max = self.maxSub(nums, begin, mid)
        right_max = self.maxSub(nums, mid, end)

        left_max_sum = -10000000
        now_sum = 0
        for i in range(mid - 1, begin - 1, -1):
            now_sum += nums[i]
            left_max_sum = now_sum if now_sum > left_max_sum else left_max_sum
        right_max_sum = -10000000
        now_sum = 0
        for i in range(mid, end):
            now_sum += nums[i]
            right_max_sum = now_sum if now_sum > right_max_sum else right_max_sum
        mid_sum = max([left_max_sum, right_max_sum,
                      left_max_sum + right_max_sum])

        return max([left_max, right_max, mid_sum])

    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSub(nums, 0, len(nums))


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([0]))
print(Solution().maxSubArray([-1]))
print(Solution().maxSubArray([-10000]))
