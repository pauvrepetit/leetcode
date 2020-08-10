# 357. 计算各个位数不同的数字个数
#
# 20200810
# huao

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        num = [10, 9*9, 9*9*8, 9*9*8*7, 9*9*8*7*6, 9*9*8*7*6*5, 9*9*8 *
               7*6*5*4, 9*9*8*7*6*5*4*3, 9*9*8*7*6*5*4*3*2, 9*9*8*7*6*5*4*3*2*1]
        count = 0
        for i in range(n):
            count += num[i]
        return count


sol = Solution()
print(sol.countNumbersWithUniqueDigits(2))
