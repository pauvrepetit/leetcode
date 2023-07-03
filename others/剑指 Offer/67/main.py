class Solution:
    def strToInt(self, str: str) -> int:
        str = str.lstrip(" ")
        if len(str) == 0:
            return 0
        neg = False
        num = 0
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            str = str[1:]
            neg = True
        for i in str:
            if i not in "0123456789":
                break
            num = num * 10 + int(i)
        if neg:
            num = -num
        if num > 0x7FFFFFFF:
            num = 0x7FFFFFFF
        if num < -0x80000000:
            num = -0x80000000
        return num