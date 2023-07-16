#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
# 5 100 1 1 1 1 1 5
#
from typing import List

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr = [[height[i], i] for i in range(len(height))]
        arr.sort()
        arr[-1].append(arr[-1][1])
        arr[-1].append(arr[-1][1])
        for i in range(len(height)-1)[::-1]:
            arr[i].append(min(arr[i][1], arr[i+1][2]))
            arr[i].append(max(arr[i][1], arr[i+1][3]))
        area = 0
        for i in range(len(height)):
            area = max(area, arr[i][0] * max(arr[i][1] - arr[i][2], arr[i][3] - arr[i][1]))
        return area

# @lc code=end

print(Solution().maxArea([5,100,1,1,1,5]))
