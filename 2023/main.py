from typing import List
#
# @lc app=leetcode.cn id=2023 lang=python3
#
# [2023] 连接后等于目标字符串的字符串对
#

# @lc code=start
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    count += 1
        return count
# @lc code=end

