from typing import List

#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        now_count = 1
        all_count = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                now_count += 1
            else:
                all_count += now_count * (now_count - 1) // 2
                now_count = 1
        all_count += now_count * (now_count - 1) // 2
        return all_count

# @lc code=end
