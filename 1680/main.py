class Solution:
    def concatenatedBinary(self, n: int) -> int:
        p = 10 ** 9 + 7
        a = 0
        i = 1
        while i <= n:
            ilen = len(bin(i)) - 2
            a = ((a << ilen) + i) % p
            i += 1
        return a

print(Solution().concatenatedBinary(12))
