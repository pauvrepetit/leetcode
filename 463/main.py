# 463. 岛屿的周长
#
# 20200909
# huao

from typing import List


def check(grid: List[List[int]], i: int, j: int) -> int:
    row = len(grid)
    column = len(grid[0])
    if row == 1 and column == 1:
        return 4
    if row == 1:
        if j == 0:
            return 4-grid[i][j+1]
        elif j == column-1:
            return 4-grid[i][j-1]
        else:
            return 4-grid[i][j-1]-grid[i][j+1]
    if column == 1:
        if i == 0:
            return 4-grid[i+1][j]
        elif i == row-1:
            return 4-grid[i-1][j]
        else:
            return 4-grid[i+1][j]-grid[i-1][j]
    if i == 0:
        if j == 0:
            return 4-grid[i+1][j]-grid[i][j+1]
        elif j == column-1:
            return 4-grid[i+1][j]-grid[i][j-1]
        else:
            return 4-grid[i+1][j]-grid[i][j-1]-grid[i][j+1]
    elif i == row-1:
        if j == 0:
            return 4-grid[i-1][j]-grid[i][j+1]
        elif j == column-1:
            return 4-grid[i-1][j]-grid[i][j-1]
        else:
            return 4-grid[i-1][j]-grid[i][j-1]-grid[i][j+1]
    else:
        if j == 0:
            return 4-grid[i+1][j]-grid[i][j+1]-grid[i-1][j]
        elif j == column-1:
            return 4-grid[i+1][j]-grid[i][j-1]-grid[i-1][j]
        else:
            return 4-grid[i+1][j]-grid[i][j-1]-grid[i][j+1]-grid[i-1][j]


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += check(grid, i, j)
        return count


print(Solution().islandPerimeter([[0, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 1, 0, 0],
                                  [1, 1, 0, 0]]))
