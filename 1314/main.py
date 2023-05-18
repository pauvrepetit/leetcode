from typing import List
#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(min(m, k+1)):
            for j in range(min(n, k+1)):
                res[0][0] += mat[i][j]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    tmp = res[i-1][j]
                    for ii in range(-k, k+1):
                        if 0 <= i-k-1 < m and 0 <= j+ii < n:
                            tmp -= mat[i-k-1][j+ii]
                        if 0 <= i+k < m and 0 <= j+ii < n:
                            tmp += mat[i+k][j+ii]
                else:
                    tmp = res[i][j-1]
                    for ii in range(-k, k+1):
                        if 0 <= i+ii < m and 0 <= j-k-1 < n:
                            tmp -= mat[i+ii][j-k-1]
                        if 0 <= i+ii < m and 0 <= j+k < n:
                            tmp += mat[i+ii][j+k]
                res[i][j] = tmp
        return res


# @lc code=end

print(Solution().matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
