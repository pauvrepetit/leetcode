import re

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0:
            return 0
        if str[0] != '+' and str[0] != '-' and (str[0] > '9' or str[0] < '0'):
            return 0
        if str[0] == '+':
            num = re.search(r'^\+\d+', str)
            if num == None:
                return 0
            else:
                num = num[0]
                num_int = int(num)
        elif str[0] == '-':
            num = re.search(r'^-\d+', str)
            if num == None:
                return 0
            else:
                num = num[0]
                num_int = int(num)
        else:
            num = re.search(r'^\d+', str)
            num = num[0]
            num_int = int(num)
        if num_int > (2 ** 31 - 1):
            return 2 ** 31 - 1
        elif num_int < -2 ** 31:
            return -2 ** 31
        else:
            return num_int

sol = Solution()
print(sol.myAtoi('+'))
print(sol.myAtoi('42'))
print(sol.myAtoi('    -42'))
print(sol.myAtoi('4211 with words'))
