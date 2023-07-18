#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        index = 1
        non_zeros = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid[i][j] = str(index)
                    non_zeros.append((i, j))
                    index += 1
                else:
                    grid[i][j] = str(0xFFFFFFF)
        changed = len(non_zeros) != 0
        while changed:
            changed = False
            for i, j in non_zeros:
                ori = int(grid[i][j])
                left = 0xFFFFFFF
                right = left
                up = left
                down = left
                if i != 0:
                    left = int(grid[i-1][j])
                    left = 0xFFFFFFF if left == 0 else left
                if j != 0:
                    up = int(grid[i][j-1])
                    up = 0xFFFFFFF if up == 0 else up
                if i != len(grid)-1:
                    right = int(grid[i+1][j])
                    right = 0xFFFFFFF if right == 0 else right
                if j != len(grid[0])-1:
                    down = int(grid[i][j+1])
                    down = 0xFFFFFFF if down == 0 else down
                new = min(left, right, up, down, ori)
                if ori != new:
                    changed = True
                    grid[i][j] = str(new)
        ccs = set()
        for i, j in non_zeros:
            ccs.add(int(grid[i][j]))
        return len(ccs)
            
# @lc code=end

print(Solution().numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))