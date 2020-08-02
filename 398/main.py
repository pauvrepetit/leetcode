# 398. 随机数索引
#
# 20200802
# huao
# 就这？

from random import randint
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.numIndex = {}
        for i in range(len(nums)):
            if nums[i] in self.numIndex.keys():
                self.numIndex[nums[i]].append(i)
            else:
                self.numIndex[nums[i]] = [i]

    def pick(self, target: int) -> int:
        targetIndex = self.numIndex[target]
        return targetIndex[randint(0, len(targetIndex)-1)]


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 3, 3, 3]
obj = Solution(nums)
print(obj.pick(1))
print(obj.pick(2))
print(obj.pick(3))
print(obj.pick(3))
print(obj.pick(3))
print(obj.pick(3))
