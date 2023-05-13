from typing import List
#
# @lc app=leetcode.cn id=2441 lang=python3
#
# [2441] 与对应负数同时存在的最大正整数
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pos_num = [0 for i in range(1001)]
        neg_num = [0 for i in range(1001)]
        max_k = -1
        for num in nums:
            if num < 0:
                neg_num[-num] = 1
            else:
                pos_num[num] = 1
            if pos_num[abs(num)] + neg_num[abs(num)] == 2:
                max_k = max(max_k, abs(num))
        return max_k
# @lc code=end

