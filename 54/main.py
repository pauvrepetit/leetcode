#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
from typing import List

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = 0
        col = 0
        end_row = len(matrix)
        end_col = len(matrix[0])
        res = []
        while row < end_row and col < end_col:
            for c in range(col, end_col):
                res.append(matrix[row][c])
            for r in range(row+1, end_row):
                res.append(matrix[r][end_col-1])
            if row != end_row-1 and col != end_col-1:
                for c in range(col, end_col-1)[::-1]:
                    res.append(matrix[end_row-1][c])
                for r in range(row+1, end_row-1)[::-1]:
                    res.append(matrix[r][col])
            row += 1
            col += 1
            end_row -= 1
            end_col -= 1
        return res

# @lc code=end

print(Solution().spiralOrder([[1,2,3,4]]))
