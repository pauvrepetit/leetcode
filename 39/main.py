# 39. 组合总和
#
# 20200909
# huao

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        return self.sol(candidates, target, [], [])

    def sol(self, candidates: List[int], target: int, numList: List[int], comb: List[List[int]]) -> List[List[int]]:
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
                comb.append(numList + [num])
            else:
                count = target // num
                for j in range(1, count+1):
                    comb = self.sol(
                        candidates[i+1:], target-num*j, numList+[num]*j, comb)
        return comb


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
print(Solution().combinationSum(candidates=[2, 3, 5], target=8))
