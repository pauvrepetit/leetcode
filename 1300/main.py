# 1300. 转变数组后最接近目标值的数组和
#
# 20200810
# huao

from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        length = len(arr)
        if length == 1:
            return min(arr[0], target)
        avg = target / length
        if avg > arr[0]:
            return self.findBestValue(arr[1:], target-arr[0])
        if target % length == 0:
            return target // length
        if (target % length) > length // 2:
            return (target // length) + 1
        else:
            return target // length
