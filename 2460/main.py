from typing import List

#
# @lc app=leetcode.cn id=2460 lang=python3
#
# [2460] 对数组执行操作
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        res = []
        count = 0
        for num in nums:
            if num != 0:
                res.append(num)
            else:
                count += 1
        for _ in range(count):
            res.append(0)
        return res
# @lc code=end

