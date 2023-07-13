from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_sum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    max_sum[i][j] = grid[i][j]
                elif i == 0:
                    max_sum[i][j] = max_sum[i][j-1] + grid[i][j]
                elif j == 0:
                    max_sum[i][j] = max_sum[i-1][j] + grid[i][j]
                else:
                    max_sum[i][j] = max(max_sum[i-1][j], max_sum[i][j-1]) + grid[i][j]
        return max_sum[-1][-1]

print(Solution().maxValue([[1]]))
