# 5511. 二进制矩阵中的特殊位置
# 周赛No.206
#
# 20200913
# huao

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            if mat[i].count(1) == 1:
                j = mat[i].index(1)
                cc = 0
                for k in range(len(mat)):
                    if mat[k][j] == 1:
                        cc += 1
                if cc == 1:
                    count += 1
        return count


print(Solution().numSpecial([[0, 0, 0, 0, 0],
                             [1, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 1, 1]]))
