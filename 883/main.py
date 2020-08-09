# 883. 三维形体投影面积
#
# 20200809
# huao

from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xLen = len(grid)
        yLen = len(grid[0])
        area = 0
        for i in range(xLen):
            maxi = 0
            for j in range(yLen):
                if grid[i][j] != 0:
                    area += 1
                maxi = max(maxi, grid[i][j])
            area += maxi
        for j in range(yLen):
            maxj = 0
            for i in range(xLen):
                maxj = max(maxj, grid[i][j])
            area += maxj
        return area


sol = Solution()
print(sol.projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
