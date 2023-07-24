#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from typing import List

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = [1 for _ in range(len(nums))]
        for i in range(1, len(length)):
            for j in range(i)[::-1]:
                if nums[j] < nums[i]:
                    length[i] = max(length[i], length[j] + 1)
        return max(length)

# @lc code=end

print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
