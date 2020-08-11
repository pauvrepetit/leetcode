# 658. 找到 K 个最接近的元素
#
# 20200811
# huao
# 总是犯些小错误...

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minLoc = self.binarySearch(arr, x, 0, len(arr))
        maxLoc = minLoc
        closestList = [arr[minLoc]]
        for i in range(1, k):
            if minLoc < 1:
                closestList.append(arr[maxLoc+1])
                maxLoc += 1
            elif maxLoc >= len(arr) - 1:
                closestList = [arr[minLoc-1]] + closestList
                minLoc -= 1
            elif (x - arr[minLoc-1]) <= (arr[maxLoc+1] - x):
                closestList = [arr[minLoc-1]] + closestList
                minLoc -= 1
            else:
                closestList.append(arr[maxLoc+1])
                maxLoc += 1
        return closestList

    def binarySearch(self, arr: List[int], x: int, begin: int, end: int) -> int:
        if begin == end:
            return begin
        elif begin + 1 == end:
            if end == len(arr):
                return begin
            elif (x - arr[begin]) <= (arr[end] - x):
                return begin
            else:
                return end
        mid = (begin + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return self.binarySearch(arr, x, mid, end)
        else:
            return self.binarySearch(arr, x, begin, mid)


sol = Solution()
print(sol.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))
