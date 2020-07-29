# 1013. 将数组分成和相等的三个部分
#
# 20200729
# huao
# 求和，从头开始找，如果和为总和的1/3，就分成一部分

from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum = 0
        for a in A:
            sum += a
        if sum % 3 != 0:
            return False

        flag = 0
        subSum = 0
        sum = sum // 3
        for a in A:
            subSum += a
            if subSum == sum:
                flag += 1
                subSum = 0
            if flag == 3:
                return True
        return False


sol = Solution()
print(sol.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(sol.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(sol.canThreePartsEqualSum([1, -1, 1, -1]))
