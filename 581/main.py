from typing import List

#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp_nums = [i for i in nums]
        tmp_nums.sort()
        diff_begin = len(nums)
        diff_end = -1
        for i in range(len(nums)):
            if nums[i] != tmp_nums[i]:
                diff_begin = i
                break
        for i in range(len(nums))[::-1]:
            if nums[i] != tmp_nums[i]:
                diff_end = i
                break
        if diff_end >= diff_begin:
            return diff_end - diff_begin + 1
        return 0
# @lc code=end

# 要O(n)的算法，想不到呀
