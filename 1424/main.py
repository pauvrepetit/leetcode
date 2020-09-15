# 1424. 对角线遍历 II
#
# 20200915
# huao
# 排序，就是有点慢

from typing import List
from functools import cmp_to_key


def cmp(x, y):
    if x[0] == y[0]:
        if x[1] > y[1]:
            return -1
        elif x[1] == y[1]:
            return 0
        else:
            return 1
    elif x[0] > y[0]:
        return 1
    else:
        return -1


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        num = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                num.append([i+j, i, nums[i][j]])

        num.sort(key=cmp_to_key(cmp))
        travel = []
        for n in num:
            travel.append(n[2])
        return travel


print(Solution().findDiagonalOrder(
    nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
