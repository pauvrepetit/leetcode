# 917. 仅仅反转字母
#
# 20200730
# huao
# 其实很简单

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        subStr = ""
        for c in S:
            if c.isalpha():
                subStr += c
        subStr = subStr[::-1]
        revStr = ""
        i = 0
        subI = 0
        while i < len(S):
            if S[i].isalpha():
                revStr += subStr[subI]
                subI += 1
            else:
                revStr += S[i]
            i += 1
        return revStr


sol = Solution()
print(sol.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
