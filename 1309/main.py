# 1309. 解码字母到整数映射
#
# 20200727
# huao
# 就是个映射而已
# 有两种情况，单个数字，两个数字后接一个#，后者优先级较高
# 判断一下就ok

class Solution:
    def freqAlphabets(self, s: str) -> str:
        sLen = len(s)
        i = 0
        chars = ""
        while i < sLen:
            if sLen - i >= 3 and s[i + 2] == '#':
                chars += chr(int(s[i:i+2]) + 0x60)
                i += 3
            else:
                chars += chr(int(s[i]) + 0x60)
                i += 1
        return chars


sol = Solution()
print(sol.freqAlphabets("1326#"))
