class Solution:
    def fib(self, n: int) -> int:
        fib_list = [0 for _ in range(105)]
        fib_list[1] = 1
        for i in range(2, n+1):
            fib_list[i] = (fib_list[i-1] + fib_list[i-2]) % 1000000007
        return fib_list[n]
