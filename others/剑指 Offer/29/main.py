from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []

        res = []
        for i in range((min(m, n) + 1) // 2):
            row_begin = i
            row_end = m - i
            col_begin = i
            col_end = n - i
            for j in range(col_begin, col_end):
                res.append(matrix[row_begin][j])
            for j in range(row_begin+1, row_end):
                res.append(matrix[j][col_end-1])
            if row_begin != row_end - 1:
                for j in range(col_begin, col_end-1)[::-1]:
                    res.append(matrix[row_end-1][j])
            if col_begin != col_end - 1:
                for j in range(row_begin+1, row_end-1)[::-1]:
                    res.append(matrix[j][col_begin])
        return res

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))