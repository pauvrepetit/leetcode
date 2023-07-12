from typing import List
from bisect import bisect_left

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            if len(line) == 0:
                return False
            if line[0] > target or line[-1] < target:
                continue
            i = bisect_left(line, target)
            if i != len(line) and line[i] == target:
                return True
        return False

print(Solution().findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
