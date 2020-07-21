# 12. 整数转罗马数字
#
# 20200721
# huao
# 理解规则，把数字划分为不同的区域即可

class Solution:
    def intToRoman(self, num: int) -> str:
        romanNum = ""
        thousand = num // 1000
        if thousand > 0:
            for i in range(thousand):
                romanNum += "M"

        num %= 1000
        hundred = num // 100
        if hundred >= 9:
            romanNum += "CM"
        elif hundred >= 5:
            romanNum += "D"
            for i in range(hundred - 5):
                romanNum += "C"
        elif hundred >= 4:
            romanNum += "CD"
        elif hundred >= 1:
            for i in range(hundred):
                romanNum += "C"
        
        num %= 100
        ten = num // 10
        if ten >= 9:
            romanNum += "XC"
        elif ten >= 5:
            romanNum += "L"
            for i in range(ten - 5):
                romanNum += "X"
        elif ten >= 4:
            romanNum += "XL"
        elif ten >= 1:
            for i in range(ten):
                romanNum += "X"
        
        num %= 10
        if num >= 9:
            romanNum += "IX"
        elif num >= 5:
            romanNum += "V"
            for i in range(num - 5):
                romanNum += "I"
        elif num >= 4:
            romanNum += "IV"
        elif num >= 1:
            for i in range(num):
                romanNum += "I"

        return romanNum


sol = Solution()
print(sol.intToRoman(1994))
