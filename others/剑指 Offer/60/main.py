# 剑指 Offer 60. n个骰子的点数
#
# 20200909
# huao
# 动态规划

from typing import List


dp = [[-1 for i in range(70)] for j in range(12)]


class Solution:
    def twoSum(self, n: int) -> List[float]:
        for i in range(1, 7):
            dp[1][i] = 1/6
        for i in range(7, 70):
            dp[1][i] = 0
        p = []
        count = 5*n+1
        for i in range(n, n*6+1):
            p.append(self.cal(n, i))
        return p

    def cal(self, i: int, j: int) -> int:
        if dp[i][j] == -1:
            dp[i][j] = 0
            for n in range(1, min(j,7)):
                dp[i][j] += self.cal(i-1, j-n)
            dp[i][j] /= 6
        return dp[i][j]


print(Solution().twoSum(2))
