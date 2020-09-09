# 41. 缺失的第一个正数
#
# 20200909
# huao

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)+1
        see = [0 for i in range(length)]
        for num in nums:
            if num >= length or num <= 0:
                continue
            see[num] = 1
        for i in range(1, length):
            if see[i] == 0:
                return i
        return length


print(Solution().firstMissingPositive([1, 3, 4, 2]))
