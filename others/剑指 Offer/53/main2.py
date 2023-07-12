from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tags = [False for _ in range(len(nums) + 1)]
        for num in nums:
            tags[num] = True
        for i in range(len(tags)):
            if not tags[i]:
                return i
