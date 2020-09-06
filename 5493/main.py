# 5493. 删除最短的子数组使剩余数组有序
# 双周赛No.34
#
# 20200905
# huao

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        start = len(arr)+1
        end = -1
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                start = min(start, i)
                end = max(end, i)
        if end == -1:
            return 0

        if start == end:
            return min(1 + self.findLengthOfShortestSubarray(arr[:start]+arr[end+1:]), 1+self.findLengthOfShortestSubarray(arr[:start+1] + arr[end+2:]))

        return end - start + self.findLengthOfShortestSubarray(arr[:start+1] + arr[end+1:])


print(Solution().findLengthOfShortestSubarray([1, 2, 3]))
print(Solution().findLengthOfShortestSubarray([1]))
print(Solution().findLengthOfShortestSubarray([10,13,17,21,15,15,9,17,22,22,13]))
print(Solution().findLengthOfShortestSubarray(
    [6, 3, 10, 11, 15, 20, 13, 3, 18, 12]))
