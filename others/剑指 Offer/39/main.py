from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = dict()
        for num in nums:
            if num in num_count.keys():
                num_count[num] += 1
            else:
                num_count[num] = 1
            if num_count[num] > len(nums) // 2:
                return num
