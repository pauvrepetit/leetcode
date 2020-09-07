# 214. 最短回文串
#
# 20200907
# huao

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s))[::-1]:
            if s[i] == s[0] and s[:i+1] == s[:i+1][::-1]:
                return s[i+1:][::-1] + s
            else:
                continue
        return s


print(Solution().shortestPalindrome("abcd"))
