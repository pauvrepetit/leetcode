# 1137. 第 N 个泰波那契数
#
# 20200916
# huao

tri = [0 for i in range(40)]


class Solution:
    def tribonacci(self, n: int) -> int:
        tri[1] = 1
        tri[2] = 1
        return self.sol(n)

    def sol(self, n: int) -> int:
        if n == 0:
            return 0
        if tri[n] == 0:
            tri[n] = self.sol(n-1) + self.sol(n-2) + self.sol(n-3)
        return tri[n]
