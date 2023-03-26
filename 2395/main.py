from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum_nums = [nums[i] + nums[i + 1] for i in range(len(nums) - 1)]
        return len(sum_nums) != len(set(sum_nums))
        # if len(sum_nums) == len(set(sum_nums)):
        #     return False
        # else:
        #     return True

print(Solution().findSubarrays(nums = [4,2,4]))
print(Solution().findSubarrays(nums = [1,2,3,4,5]))
print(Solution().findSubarrays(nums = [0,0,0]))
