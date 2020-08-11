# 1295. 统计位数为偶数的数字
#
# 20200811
# huao

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            count += (self.countNum(num) + 1) % 2
        return count

    def countNum(self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            num //= 10
        return count


sol = Solution()
print(sol.findNumbers([12, 345, 2, 6, 7896]))
