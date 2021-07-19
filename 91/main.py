# 91. 解码方法
#
# 20210719
# huao
# 分治法

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        if len(s) == 1 and s != '0':
            return 1
        if s == '0':
            return 0
        mid = len(s) // 2
        left_s = s[:mid]
        right_s = s[mid:]
        count = self.numDecodings(left_s) * self.numDecodings(right_s)
        ano_left_s = s[:mid - 1]
        ano_right_s = s[mid + 1:]
        if s[mid-1] != '0' and int(s[mid-1:mid+1]) <= 26:
            count += self.numDecodings(ano_left_s) * self.numDecodings(ano_right_s)
        return count

print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("0"))
print(Solution().numDecodings("02"))
print(Solution().numDecodings("111111111111111111111111111111111111111111111"))
