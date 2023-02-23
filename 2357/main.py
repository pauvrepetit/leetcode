from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return (len(set(nums)) - 1) if 0 in nums else len(set(nums))

print(Solution().minimumOperations([1,5,0,3,5]))
