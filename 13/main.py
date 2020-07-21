# 13. 罗马数字转整数
#
# 20200721
# huao
# 只是根据规则解析字符串而已

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        while s.startswith('M'):
            num += 1000
            s = s[1:]
        
        if s.startswith('CM'):
            num += 900
            s = s[2:]
        elif s.startswith('CD'):
            num += 400
            s = s[2:]
        elif s.startswith('D'):
            num += 500
            s = s[1:]
        
        while s.startswith('C'):
            num += 100
            s = s[1:]

        if s.startswith('XC'):
            num += 90
            s = s[2:]
        elif s.startswith('XL'):
            num += 40
            s = s[2:]
        elif s.startswith('L'):
            num += 50
            s = s[1:]
        
        while s.startswith('X'):
            num += 10
            s = s[1:]

        if s.startswith('IX'):
            num += 9
            s = s[2:]
        elif s.startswith('IV'):
            num += 4
            s = s[2:]
        elif s.startswith('V'):
            num += 5
            s = s[1:]
        
        while s.startswith('I'):
            num += 1
            s = s[1:]

        return num


sol = Solution()
print(sol.romanToInt("MCMXCIV"))
