# 50. Pow(x, n)
#
# 20200728
# huao
# 直接用 ** 运算符
# 二分 乘法
# leetcode的时间抖动很大呀

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n % 2 == 0:
            p = self.myPow(x, n // 2)
            return p * p
        else:
            p = self.myPow(x, n // 2)
            return p * p * x

        # return x ** n


sol = Solution()
print(sol.myPow(2.00000, 10))
