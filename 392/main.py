# 392. 判断子序列
#
# 20200727
# huao
# 两个指针把两个串扫一遍，就可以了

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        sCount = 0
        tCount = 0
        while sCount < sLen and tCount < tLen:
            if t[tCount] == s[sCount]:
                sCount += 1
                tCount += 1
                continue
            while tCount < tLen and t[tCount] != s[sCount]:
                tCount += 1
        if sCount == sLen:
            return True
        else:
            return False


sol = Solution()
print(sol.isSubsequence("abc", "ababab"))
