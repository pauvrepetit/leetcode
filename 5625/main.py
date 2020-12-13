# 5625. 比赛中的配对次数

class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n % 2 == 0:
            return self.numberOfMatches(n // 2) + n // 2
        else:
            return self.numberOfMatches(n // 2 + 1) + n // 2
