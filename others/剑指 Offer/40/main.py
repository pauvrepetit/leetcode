# 剑指 Offer 40. 最小的k个数
#
# 20200916
# huao

from typing import List

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]