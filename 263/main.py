# 263. 丑数
#
# 20200801
# huao
# 只包含质因数 2, 3, 5 的正整数

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        if num == 1:
            return True
        else:
            return False