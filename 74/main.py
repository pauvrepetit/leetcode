# 74. 搜索二维矩阵
#
# 20200907
# huao

from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixList = sum(matrix, [])
        c = bisect.bisect_left(matrixList, target)
        if c != len(matrixList) and matrixList[c] == target:
            return True
        else:
            return False
    # 下面也是对的，但是更麻烦，还更慢
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     if len(matrix) == 0 or len(matrix[0]) == 0:
    #         return False
    #     col = [matrix[i][0] for i in range(len(matrix))]
    #     c = bisect.bisect_left(col, target)
    #     if c != len(col) and col[c] == target:
    #         return True
    #     elif c == 0:
    #         return False
    #     else:
    #         r = bisect.bisect_left(matrix[c-1], target)
    #         if r != len(matrix[0]) and matrix[c-1][r] == target:
    #             return True
    #         else:
    #             return False


print(Solution().searchMatrix([[1]], 1))
