# 面试题 01.06. 字符串压缩
#
# 20200725
# huao
# 这是个简单题

class Solution:
    def compressString(self, S: str) -> str:
        nowChar = '-'
        nowCount = 0
        resStr = ""
        for c in S:
            if c == nowChar:
                nowCount += 1
            elif nowChar != '-':
                resStr += (nowChar + str(nowCount))
                nowChar = c
                nowCount = 1
            else:
                nowChar = c
                nowCount = 1
        resStr += (nowChar + str(nowCount))
        if len(resStr) < len(S):
            return resStr
        else:
            return S


sol = Solution()
print(sol.compressString("aabcccccaaa"))
