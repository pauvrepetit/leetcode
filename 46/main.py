# 46. 全排列
#
# 20200917
# huao

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        numList = []
        for i in range(len(nums)):
            subList = self.permute(nums[:i] + nums[i+1:])
            for sub in subList:
                numList.append([nums[i]] + sub)
        return numList


print(Solution().permute([1, 2, 3]))
