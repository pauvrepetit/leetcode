# 738. 单调递增的数字
# 这写法我自己都觉得很迷

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = str(N)
        ss = ''
        for i in range(len(s)-1):
            ss += s[i]
            if s[i] > s[i+1]:
                ss = str(self.monotoneIncreasingDigits(int(ss) - 1))
                ss += '9' * (len(s)-i-1)
                return int(ss)
        return N


print(Solution().monotoneIncreasingDigits(10))
print(Solution().monotoneIncreasingDigits(1234))
print(Solution().monotoneIncreasingDigits(332))
print(Solution().monotoneIncreasingDigits(123212321))
