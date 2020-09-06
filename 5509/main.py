# 5509. 避免重复字母的最小删除成本
# 周赛No.205
#
# 20200906
# huao

from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = 0
        allCost = 0
        while i < len(s):
            if i < len(s)-1 and s[i] == s[i+1]:
                tempAllCost = 0
                maxCost = -1
                for j in range(i, len(s)):
                    if s[i] == s[j]:
                        tempAllCost += cost[j]
                        maxCost = max(maxCost, cost[j])
                    else:
                        i = j
                        break
                else:
                    i = len(s)-1
                allCost += (tempAllCost - maxCost)
            else:
                i += 1
        return allCost


print(Solution().minCost(s="abaac", cost=[1, 2, 3, 4, 5]))
print(Solution().minCost(s="abc", cost=[1, 2, 3]))
print(Solution().minCost(s="aabaa", cost=[1, 2, 3, 4, 1]))
