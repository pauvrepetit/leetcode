# 面试题 17.14. 最小K个数
#
# 20200726
# huao
# emmm...
# 这配得上"中等"二字？

from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]


sol = Solution()
print(sol.smallestK([1, 2, 3], 0))
