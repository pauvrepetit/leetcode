# 28. 实现 strStr()
#
# 20200722
# huao
# 找子串第一次出现的位置
# 字符串是否以另一个字符串开头的判定函数在python、java中都是存在的吧

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:].startswith(needle):
                return i
        return -1
