#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
# 用堆来维护，其实和我们在15445里面写的那个sort -> top-n的优化策略是非常类似的
# 只是说这里堆里面的数据需要维护一个索引，来做出堆的操作
#
from typing import List
import heapq

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        res = [-heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res

# @lc code=end

print(Solution().maxSlidingWindow([1, -1], 1))