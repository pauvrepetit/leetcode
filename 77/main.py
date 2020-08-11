# 77. 组合
#
# 20200811
# huao
# 递归

from typing import List


class Solution:
    def combine(self, n: int, k: int, level=1) -> List[List[int]]:
        if n == k:
            return [[i+level for i in range(k)]]
        if k == 0:
            return []
        contain = self.combine(n-1, k-1, level+1)
        for i in range(len(contain)):
            contain[i] = [level] + contain[i]
        if contain == []:
            contain = [[level]]
        return contain + self.combine(n-1, k, level+1)


sol = Solution()
print(sol.combine(4, 2))
