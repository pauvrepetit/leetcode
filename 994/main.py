#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
from typing import List

# @lc code=start
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bad_list = Queue()
        good_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    bad_list.put((i, j, 0))
                if grid[i][j] == 1:
                    good_count += 1
        time = 0
        while not bad_list.empty():
            i, j, now = bad_list.get()
            time = max(time, now)
            if i != 0 and grid[i-1][j] == 1:
                bad_list.put((i-1, j, now+1))
                grid[i-1][j] = 2
                good_count -= 1
            if j != 0 and grid[i][j-1] == 1:
                bad_list.put((i, j-1, now+1))
                grid[i][j-1] = 2
                good_count -= 1
            if i != len(grid)-1 and grid[i+1][j] == 1:
                bad_list.put((i+1, j, now+1))
                grid[i+1][j] = 2
                good_count -= 1
            if j != len(grid[0])-1 and grid[i][j+1] == 1:
                bad_list.put((i, j+1, now+1))
                grid[i][j+1] = 2
                good_count -= 1
        if good_count == 0:
            return time
        return -1
        
# @lc code=end

