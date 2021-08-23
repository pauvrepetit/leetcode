# 215. 数组中的第K个最大元素
#
# 20210823
# huao
# 我知道，这个题算法导论上有讲过，找第k大的元素，时间复杂度好像比排序要快吧，不会写...

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
