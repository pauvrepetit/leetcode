from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 记录当前位置的最大子数组和，以及以当前位置结束的最大子数组和
        n = len(nums)
        max_sum = [0 for _ in range(n)]
        now_max_sum = [0 for _ in range(n)]
        max_sum[0] = nums[0]
        now_max_sum[0] = nums[0]
        for i in range(1, n):
            now_max_sum[i] = max(now_max_sum[i-1]+nums[i], nums[i])
            max_sum[i] = max(max_sum[i-1], now_max_sum[i])
        return max_sum[-1]
