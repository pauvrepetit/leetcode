#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from typing import List

# @lc code=start
class Solution:
    def dfs(self, board: List[List[str]], visited: List[List[bool]], word: str, i: int, j: int) -> bool:
        if word == "":
            return True
        if board[i][j] != word[0]:
            return False
        if visited[i][j]:
            return False
        if len(word) == 1:
            return True
        visited[i][j] = True
        if i != 0 and self.dfs(board, visited, word[1:], i-1, j):
            return True
        if j != 0 and self.dfs(board, visited, word[1:], i, j-1):
            return True
        if i != len(board)-1 and self.dfs(board, visited, word[1:], i+1, j):
            return True
        if j != len(board[0])-1 and self.dfs(board, visited, word[1:], i, j+1):
            return True
        visited[i][j] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                visited = [[False for _ in range(n)] for _ in range(m)]
                if self.dfs(board, visited, word, i, j):
                    return True
        return False

# @lc code=end

print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
