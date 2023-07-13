from typing import List

#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        path_sum = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            path_sum[-1][i] = matrix[-1][i]
        for i in range(n-1)[::-1]:
            for j in range(n):
                # 给path_sum[i][j]赋值
                if j == 0:
                    path_sum[i][j] = matrix[i][j] + min(path_sum[i+1][j], path_sum[i+1][j+1])
                elif j == n-1:
                    path_sum[i][j] = matrix[i][j] + min(path_sum[i+1][j-1], path_sum[i+1][j])
                else:
                    path_sum[i][j] = matrix[i][j] + min(path_sum[i+1][j-1], path_sum[i+1][j], path_sum[i+1][j+1])
        return min(path_sum[0])

# @lc code=end

