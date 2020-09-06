# 5491. 矩阵对角线元素的和
# 双周赛No.34
#
# 20200905
# huao

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        length = len(mat)
        for i in range(length):
            sum += mat[i][i]
            sum += mat[i][length-i-1]
        if length % 2 == 1:
            sum -= mat[length // 2][length // 2]
        return sum


print(Solution().diagonalSum(mat=[[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]]))
print(Solution().diagonalSum(mat=[[1, 1, 1, 1],
                                  [1, 1, 1, 1],
                                  [1, 1, 1, 1],
                                  [1, 1, 1, 1]]))
print(Solution().diagonalSum(mat=[[5]]))
