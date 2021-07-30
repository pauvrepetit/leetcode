# 202. 快乐数
#
# 20210730
# huao
# 并不快乐

class Solution:
    def sum_n(self, n: int) -> int:
        sn = str(n)
        s = 0
        for c in sn:
            c = int(c)
            s += c ** 2
        return s

    def isHappy(self, n: int) -> bool:
        happy = [0 for i in range(1000)]
        n = self.sum_n(n)
        while happy[n] == 0 and n != 1:
            happy[n] = 1
            n = self.sum_n(n)
        if n == 1:
            return True
        return False
