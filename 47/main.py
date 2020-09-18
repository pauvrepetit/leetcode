# 47. 全排列 II
#
# 20200918
# huao

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        numList = []
        for i in range(len(nums)):
            subList = self.permuteUnique(nums[:i] + nums[i+1:])
            for sub in subList:
                if [nums[i]] + sub not in numList:
                    numList.append([nums[i]] + sub)
        return numList


print(Solution().permuteUnique([1, 1, 2])