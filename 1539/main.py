# 1539. 第 k 个缺失的正整数
#
# 20200810
# huao

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        begin = 0
        num = 0
        i = 0
        while i < k:
            num += 1
            if begin < len(arr) and num == arr[begin]:
                begin += 1
            else:
                i += 1
        return num


sol = Solution()
print(sol.findKthPositive([2, 3, 4, 7, 11], 5))
