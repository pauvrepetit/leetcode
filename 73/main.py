# 73. 矩阵置零
#
# 20210716
# huao

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        matrix_000 = 1
        matrix_001 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0:
                        matrix_000 = 0
                    else:
                        matrix[i][0] = 0
                    if j == 0:
                        matrix_001 = 0
                    else:
                        matrix[0][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
        if matrix[0][0] == 0 or (matrix_000 == 0 and matrix_001 == 0):
            for i in range(len(matrix)):
                matrix[i][0] = 0
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        elif matrix_000 == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        elif matrix_001 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        return


matrix = [[8, 3, 6, 9, 7, 8, 0, 6],
          [0, 3, 7, 0, 0, 4, 3, 8],
          [5, 3, 6, 7, 1, 6, 2, 6],
          [8, 7, 2, 5, 0, 6, 4, 0],
          [0, 2, 9, 9, 3, 9, 7, 3]]
Solution().setZeroes(matrix)
print(matrix)
