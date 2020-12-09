from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        begin = 0
        end = len(nums) - 1
        count = 0
        while begin < end:
            if nums[begin] + nums[end] == k:
                count += 1
                begin += 1
                end -= 1
            elif nums[begin] + nums[end] > k:
                end -= 1
            else:
                begin += 1
        return count
