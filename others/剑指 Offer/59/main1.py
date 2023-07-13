from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        heap = []
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))
        res = []
        for i in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while True:
                max_val = heapq.heappop(heap)
                if max_val[1] >= i - k + 1:
                    heapq.heappush(heap, max_val)
                    res.append(-max_val[0])
                    break
        return res

print(Solution().maxSlidingWindow([1,-1], 1))