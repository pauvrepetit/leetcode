import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            left = c - i ** 2
            tmp = int(math.sqrt(left))
            if tmp ** 2 == left:
                return True
        return False


for i in range(1, 6):
    print(Solution().judgeSquareSum(i))
