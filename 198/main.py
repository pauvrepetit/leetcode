#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sum = []
        for i in range(len(nums)):
            if i == 0:
                sum.append(nums[0])
            elif i == 1:
                sum.append(nums[1])
            elif i == 2:
                sum.append(nums[0] + nums[2])
            else:
                sum.append(max(sum[i-2], sum[i-3]) + nums[i])
        return max(sum[-1], sum[-2])

# @lc code=end

print(Solution().rob([1,2,3,1]))
