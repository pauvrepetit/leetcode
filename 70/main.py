# 70. 爬楼梯
#
# 20210716
# huao


from math import comb


class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        for i in range(n // 2 + 1):
            count += comb(n - i, i)
        return count


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
