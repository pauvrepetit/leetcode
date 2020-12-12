# 376. 摆动序列
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        i = 0
        # 去重
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums = nums[:i] + nums[i+1:]
            else:
                i += 1
        
        numsLen = len(nums)
        if numsLen <= 2:
            return numsLen

        up = (nums[0] < nums[1])
        i = 1
        while i < len(nums) - 1:
            if (nums[i-1] < nums[i] and nums[i] < nums[i+1]) or (nums[i-1] > nums[i] and nums[i] > nums[i+1]):
                nums = nums[:i] + nums[i+1:]
            else:
                i += 1
        return len(nums)

print(Solution().wiggleMaxLength([0, 0, 0]))