# 69. x 的平方根
#
# 20200730
# huao
# 手算开方
# 不知道库函数是怎么实现的
# 我们就简单的写了一个二分法

from math import sqrt


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1
        begin = 1
        end = x
        while True:
            num = (begin + end) // 2
            if num * num <= x and (num + 1) * (num + 1) > x:
                return num
            elif num * num > x:
                end = num
            else:
                begin = num


sol = Solution()
for i in range(1024):
    realRes = int(sqrt(i))
    myRes = sol.mySqrt(i)
    print(str(realRes) + str(myRes) + str(realRes == myRes))
