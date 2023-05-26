from typing import List
#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
import queue

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        shortestLength = [[-1 for _ in range(n)] for _ in range(n)]
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        shortestLength[0][0] = 1
        frontier = queue.Queue()
        frontier.put([0, 0])
        while not frontier.empty():
            a, b = frontier.get()
            if grid[a][b] == 0 and shortestLength[a][b] != -1:
                next_node_list = [[a-1, b-1], [a-1, b], [a-1, b+1], [a, b-1], [a, b], [a, b+1], [a+1, b-1], [a+1, b], [a+1, b+1]]
                for next_a, next_b in next_node_list:
                    if next_a < 0 or next_a >= n or next_b < 0 or next_b >= n:
                        continue
                    if grid[next_a][next_b] == 0 and shortestLength[next_a][next_b] == -1:
                        shortestLength[next_a][next_b] = shortestLength[a][b] + 1
                        frontier.put([next_a, next_b])
        return shortestLength[-1][-1]

# @lc code=end

print(Solution().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
