# 65. 有效数字
#
# 20200912
# huao

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False