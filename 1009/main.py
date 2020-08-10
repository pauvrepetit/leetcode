# 1009. 十进制整数的反码
#
# 20200810
# huao

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        i = 0
        while N >= (2 << i):
            i += 1
        return (2 << i) - N - 1
