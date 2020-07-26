# 1392. 最长快乐前缀
#
# 20200726
# huao
# 就穷举呗，怎么能更快呢...

class Solution:
    def longestPrefix(self, s: str) -> str:
        sLen = len(s)
        for i in range(sLen)[::-1]:
            if s[:i] == s[sLen - i:]:
                return s[:i]
        return ""


sol = Solution()
print(sol.longestPrefix("aaaaa"))
