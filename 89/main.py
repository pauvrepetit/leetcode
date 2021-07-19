# 89. 格雷编码
#
# 20210719
# huao
# Gray Code, 虽然我们在组原课里面讲过，但很显然我都忘了

from typing import List


class Solution:
    def trans(self, n: int) -> int:
        ns = '0' + bin(n)[2:]
        gs = ''
        for i in range(len(ns) - 1):
            if ns[i] == ns[i + 1]:
                gs += '0'
            else:
                gs += '1'
        return int(gs, 2)

    def grayCode(self, n: int) -> List[int]:
        gray = [i for i in range(2 ** n)]
        for i in range(len(gray)):
            gray[i] = self.trans(gray[i])
        return gray


print(Solution().grayCode(2))
print(Solution().grayCode(0))
