from typing import List
from math import sqrt

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        target <<= 1
        divide_stack = []
        for i in range(2, int(sqrt(target)) + 1):
            if target % i == 0:
                if i % 2 != 0 or target // i % 2 != 0:
                    divide_stack.append((i, target // i))

        res = []
        for x, y in divide_stack[::-1]:
            min_val = (y + 1 - x) >> 1
            max_val = (y - 1 + x) >> 1
            if min_val >= 1:
                res.append(list(range(min_val, max_val + 1)))

        for y, x in divide_stack:
            min_val = (y + 1 - x) >> 1
            max_val = (y - 1 + x) >> 1
            if min_val >= 1:
                res.append(list(range(min_val, max_val + 1)))
        return res

print(Solution().findContinuousSequence(10))
