# 40. 组合总和 II
#
# 20200909
# huao

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        return self.sol(candidates, target, [], [])

    def sol(self, candidates:  List[int], target: int, numList: List[int], comb: List[List[int]]) -> List[List[int]]:
        if target == 0:
            comb.append(numList)
            return comb
        if len(candidates) == 0:
            return comb
        for i in range(len(candidates)):
            num = candidates[i]
            if num > target:
                continue
            elif num == target:
                if (numList+[num]) in comb:
                    continue
                comb.append(numList + [num])
            else:
                comb = self.sol(candidates[i+1:],
                                target-num, numList+[num], comb)
        return comb


print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
