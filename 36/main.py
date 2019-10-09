from typing import List

class Solution:
    def checkRow(self, board: List[List[str]]) -> bool:
        zeroList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            checkList = zeroList[:]
            for j in range(9):
                if board[i][j] != '.':
                    if checkList[int(board[i][j])] == 1:
                        return False
                    else:
                        checkList[int(board[i][j])] += 1
        return True
    def checkColumn(self, board: List[List[str]]) -> bool:
        zeroList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            checkList = zeroList[:]
            for i in range(9):
                if board[i][j] != '.':
                    if checkList[int(board[i][j])] == 1:
                        return False
                    else:
                        checkList[int(board[i][j])] += 1
        return True
    def checkBlock(self, board: List[List[str]]) -> bool:
        zeroList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(3):
            for j in range(3):
                checkList = zeroList[:]
                for k in range(3):
                    for l in range(3):
                        if board[i * 3 + k][j * 3 + l] != '.':
                            if checkList[int(board[i * 3 + k][j * 3 + l])] == 1:
                                return False
                            else:
                                checkList[int(board[i * 3 + k][j * 3 + l])] += 1
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.checkRow(board) and self.checkColumn(board) and self.checkBlock(board):
            return True
        else:
            return False

sol = Solution()
sudoku1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
sudoku2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(sol.isValidSudoku(sudoku1))
print(sol.isValidSudoku(sudoku2))
