from typing import List

class Solution:
    def dfs(self, board: List[List[str]], visited: List[List[bool]], r: int, c: int, word: str, index: int) -> bool:
        row_size = len(board)
        col_size = len(board[0])
        visited[r][c] = True
        index += 1
        if index == len(word):
            return True
        # r-1 c | r+1 c | r c-1 | r c+1
        if r >= 1 and not visited[r-1][c] and board[r-1][c] == word[index]:
            if self.dfs(board, visited, r-1, c, word, index):
                return True
        if r+1 < row_size and not visited[r+1][c] and board[r+1][c] == word[index]:
            if self.dfs(board, visited, r+1, c, word, index):
                return True
        if c >= 1 and not visited[r][c-1] and board[r][c-1] == word[index]:
            if self.dfs(board, visited, r, c-1, word, index):
                return True
        if c+1 < col_size and not visited[r][c+1] and board[r][c+1] == word[index]:
            if self.dfs(board, visited, r, c+1, word, index):
                return True
        visited[r][c] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    visited = [[False for _ in board[0]] for _ in board]
                    if self.dfs(board, visited, r, c, word, 0):
                        return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))