# 1310. 子数组异或查询
#
# 20200801
# huao
# ???

from typing import List
from functools import cmp_to_key
from math import fabs


def cmp(x: List[int], y: List[int]) -> int:
    if x[0] == y[0]:
        return x[1] - y[1]
    else:
        return x[0] - y[0]


class Solution:
    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    #     xorArr = []
    #     for query in queries:
    #         xor = 0
    #         for i in range(query[0], query[1] + 1):
    #             xor = xor ^ arr[i]
    #         xorArr.append(xor)
    #     return xorArr
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=cmp_to_key(cmp))
        if queries == []:
            return []
        lastQuery = queries[0]
        xor = 0
        xorArr = [0 for i in range(len(queries))]
        for i in range(lastQuery[0], lastQuery[1] + 1):
            xor = xor ^ arr[i]
        xorArr[lastQuery[2]] = xor
        for query in queries[1:]:
            if query[0] == lastQuery[0]:
                for i in range(lastQuery[1]+1, query[1]+1):
                    xor = xor ^ arr[i]
            else:
                if int(fabs(lastQuery[1] - query[1])+0.5) + query[0] - lastQuery[0] < query[1] - query[0]:
                    for i in range(lastQuery[0], query[0]):
                        xor = xor ^ arr[i]
                    if lastQuery[1] < query[1]:
                        for i in range(lastQuery[1]+1, query[1]+1):
                            xor = xor ^ arr[i]
                    else:
                        for i in range(query[1]+1, lastQuery[1]+1):
                            xor = xor ^ arr[i]
                else:
                    xor = 0
                    for i in range(query[0], query[1]+1):
                        xor = xor ^ arr[i]
            xorArr[query[2]] = xor
            lastQuery = query
        return xorArr


sol = Solution()
print(sol.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))
