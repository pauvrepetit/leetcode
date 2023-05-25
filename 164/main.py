from typing import List
from collections import OrderedDict

#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_sub = 0
        for i in range(len(nums) - 1):
            max_sub = max(max_sub, abs(nums[i+1] - nums[i]))
        return max_sub
# @lc code=end

print(Solution().maximumGap([3,6,9,1]))
