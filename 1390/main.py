# 1390. 四因数
#
# 20200729
# huao
# 就检查每个数 如果满足条件就加进去就ok

from typing import List
from math import sqrt


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += self.check(num)
        return sum

    def check(self, num: int) -> bool:
        count = 2
        sum = 1 + num
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0 and num // i != i:
                count += 2
                sum += i + num // i
                if count > 4:
                    return 0
            elif num % i == 0 and num // i == i:
                return 0
        if count == 4:
            return sum
        else:
            return 0


sol = Solution()
print(sol.sumFourDivisors([21, 1, 2, 3, 4]))
