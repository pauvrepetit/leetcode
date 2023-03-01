from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # 题目保证了矩阵是一个方阵
        n = len(grid)
        maxLocal = [[max(grid[j][i:i+3] + grid[j+1][i:i+3] + grid[j+2][i:i+3]) for i in range(n-2)] for j in range(n-2)]
        return maxLocal

print(Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
print(Solution().largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
