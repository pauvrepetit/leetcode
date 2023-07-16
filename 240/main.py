#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
from typing import List
import bisect

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # cols = [matrix[i][0] for i in range(len(matrix))]
        # index = bisect.bisect_left(cols, target)
        # if cols[index] == target:
        #     return True
        for i in range(len(matrix)):
            j = bisect.bisect_left(matrix[i], target)
            if j < len(matrix[i]) and matrix[i][j] == target:
                return True
        return False
        
# @lc code=end

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
