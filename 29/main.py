# 29. 两数相除
#
# 20200722
# huao
# 不用乘法、除法和取模运算，求两数除法的结果(整数部分)
# 这就是组原里面讲过的乘除法的计算，虽然手头没有书，但还是记得一些的
# 关于溢出的问题，组原课上算是没有详细讲啊

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        sign = 0
        if dividend < 0 and divisor > 0:
            sign = 1
            dividend = -dividend
        elif dividend > 0 and divisor < 0:
            sign = 1
            divisor = -divisor
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor

        num1Len = len(bin(dividend)) - 2
        num2Len = len(bin(divisor)) - 2

        if num1Len < num2Len:
            return 0

        divisor <<= (num1Len - num2Len)
        divResult = 0

        for i in range(num1Len - num2Len + 1):
            if dividend >= divisor:
                divResult += 1
                dividend -= divisor
            divResult <<= 1
            divisor >>= 1

        divResult >>= 1
        if sign == 1:
            divResult = -divResult

        if divResult > ((1 << 31) - 1) or divResult < -(1 << 31):
            return ((1 << 31) - 1)
        else:
            return divResult


sol = Solution()
print(sol.divide(-2147483648, 1))
