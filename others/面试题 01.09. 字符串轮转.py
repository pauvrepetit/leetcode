# 面试题 01.09. 字符串轮转
#
# 20200728
# huao
# 遍历每个可以分割的位置，字符串分割成两部分，比较即可

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        s2Len = len(s2)
        if s1Len != s2Len:
            return False
        if s1Len == 0:
            return True
        for i in range(s1Len):
            if s1[:i] == s2[s2Len-i:] and s1[i:] == s2[:s2Len-i]:
                return True
        return False


sol = Solution()
print(sol.isFlipedString("ab", "aba"))
