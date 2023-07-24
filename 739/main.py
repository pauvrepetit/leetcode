#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
from typing import List

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in temperatures]
        i = 0
        while i < len(temperatures):
            if len(stack) == 0:
                stack.append((temperatures[i], i))
                i += 1
            elif temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            else:
                stack.append((temperatures[i], i))
                i += 1
        return res

# @lc code=end

