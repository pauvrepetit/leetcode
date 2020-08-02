# 343. 整数拆分
# 剑指 Offer 14- I. 剪绳子
#
# 20200802
# huao
# 假设将其分成k份 那么要使成绩最大，必须保证任意两个数的差均为0或1
# 否则，若为2，则可变为0，根据基本不等式，成绩将变大
# 那么我们穷举每种可能的份数k，就可以得到最大的乘积

class Solution:
    def cuttingRope(self, n: int) -> int:
        maxMul = n - 1
        for i in range(2, n):
            base = n // i
            left = n % i
            maxMul = max(maxMul, base ** (i - left) * (base + 1) ** left)
        return maxMul


sol = Solution()
print(sol.cuttingRope(10))
