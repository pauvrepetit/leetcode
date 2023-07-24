#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
from math import sqrt

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        counts = [0, 1]
        for i in range(2, n+1):
            count = i
            for j in range(2, int(sqrt(i))+1):
                count = min(count, counts[i-j*j]+1)
            counts.append(count)
        return counts[-1]

# @lc code=end

print(Solution().numSquares(13))
