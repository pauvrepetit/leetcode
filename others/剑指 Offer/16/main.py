class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.myPow(1/x, -n)
        tmp = self.myPow(x, n // 2)
        if n % 2 == 1:
            return tmp * tmp * x
        return tmp * tmp