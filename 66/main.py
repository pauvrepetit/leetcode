# 66. 加一
#
# 20200730
# huao
# 用list表示的数字做加一的操作
# 无非就是遇到9时候的进位操作

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsLen = len(digits)
        if digitsLen == 1 and digits[0] == 9:
            return [1, 0]
        if digits[digitsLen - 1] != 9:
            digits[digitsLen - 1] += 1
            return digits
        else:
            digits = self.plusOne(digits[:digitsLen-1])
            digits.append(0)
            return digits


sol = Solution()
print(sol.plusOne([1, 2, 3]))
print(sol.plusOne([4, 3, 2, 1]))
print(sol.plusOne([9, 9, 9]))
