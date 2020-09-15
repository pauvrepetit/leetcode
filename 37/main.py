# 37. 解数独
#
# 20200915
# huao
# 其实就是一个简单的回溯，两年前这就是我们两周的课设的内容，现在看来不过是半小时的工作量，三四十行代码的东西...

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.sol(board)
        return

    def sol(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    possibleNum = self.getPossibleNum(board, i, j)
                    for n in possibleNum:
                        board[i][j] = n
                        if self.sol(board) == True:
                            return True
                    board[i][j] = '.'
                    return False
        return True

    def getPossibleNum(self, board: List[List[str]], i: int, j: int) -> List[int]:
        possibleNums = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        unPossiableNums = set([])
        for ii in range(9):
            if board[i][ii] != '.':
                unPossiableNums.add(board[i][ii])
        for jj in range(9):
            if board[jj][j] != '.':
                unPossiableNums.add(board[jj][j])
        i = i // 3 * 3
        j = j // 3 * 3
        for ii in range(3):
            for jj in range(3):
                if board[ii+i][jj+j] != '.':
                    unPossiableNums.add(board[ii+i][jj+j])
        return list(possibleNums - unPossiableNums)


print(Solution().sol([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                      [".", "9", "8", ".", ".", ".", ".", "6", "."],
                      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                      [".", "6", ".", ".", ".", ".", "2", "8", "."],
                      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
