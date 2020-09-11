# 216. 组合总和 III
#
# 20200911
# huao

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        return self.sol(candidates, n, [], [], k)

    def sol(self, candidates:  List[int], target: int, numList: List[int], comb: List[List[int]], k: int) -> List[List[int]]:
        if target == 0:
            if len(numList) == k:
                comb.append(numList)
            return comb
        if len(candidates) == 0:
            return comb
        for i in range(len(candidates)):
            num = candidates[i]
            if num > target:
                continue
            elif num == target:
                if len(numList) == k - 1:
                    comb.append(numList + [num])
            else:
                comb = self.sol(candidates[i+1:],
                                target-num, numList+[num], comb, k)
        return comb
