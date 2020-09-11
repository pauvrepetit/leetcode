# 704. 二分查找
#
# 20200911
# huao

import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        loc = bisect.bisect_left(nums, target)
        if loc == len(nums) or nums[loc] != target:
            return -1
        else:
            return loc


print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=1000))
