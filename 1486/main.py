# 1486. 数组异或操作
#
# 20200811
# huao

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num = 0
        i = 0
        while i < n:
            num = num ^ start
            start += 2
            i += 1
        return num
