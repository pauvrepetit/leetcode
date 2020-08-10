# 55. 跳跃游戏
#
# 20200810
# huao

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        reach = [0 for i in range(len(nums))]
        reach[0] = 1
        maxReach = 0
        i = 0
        while i < len(nums):
            if i <= maxReach:
                maxReach = max(nums[i] + i, maxReach)
            i += 1
        return maxReach >= len(nums) - 1


sol = Solution()
print(sol.canJump([3, 2, 1, 0, 4]))
