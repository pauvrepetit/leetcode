class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        str_n = bin(n)[2:]
        return len(str_n) % 2 == 1 and str_n.count("1") == 1

print(Solution().isPowerOfFour(1))
print(Solution().isPowerOfFour(2))
print(Solution().isPowerOfFour(4))
print(Solution().isPowerOfFour(8))
print(Solution().isPowerOfFour(16))
