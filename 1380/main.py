# 1380. 矩阵中的幸运数
#
# 20200802
# huao
# 先找每行的最小值 然后判断该值是不是这一列中的最大值

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        luckyNumList = []
        for rowNum in range(len(matrix)):
            row = matrix[rowNum]
            columnNum = self.getMin(row)
            if self.checkColumn(matrix, rowNum, columnNum):
                luckyNumList.append(row[columnNum])
        return luckyNumList

    def getMin(self, row: List[int]) -> int:
        minNum = 10 ** 6
        minColumn = 0
        for i in range(len(row)):
            if minNum > row[i]:
                minNum = row[i]
                minColumn = i
        return minColumn

    def checkColumn(self, matrix: List[List[int]], row: int, column: int) -> bool:
        num = matrix[row][column]
        for i in range(len(matrix)):
            if num < matrix[i][column]:
                return False
        return True


sol = Solution()
print(sol.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
