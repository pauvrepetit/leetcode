from typing import List
import bisect

class Solution:
    def search_break(self, arr: List[int]) -> int:
        begin, end = 0, len(arr)
        mid = (begin + end) // 2
        while begin != mid:
            if arr[mid] < arr[-1]:
                end = mid
            elif arr[mid] > arr[0]:
                begin = mid
            else:
                return -1
            mid = (begin + end) // 2
        return begin

    def search(self, arr: List[int], target: int) -> int:
        mid = self.search_break(arr)
        if mid == -1:
            for i in range(len(arr)):
                if arr[i] == target:
                    return i
        if target >= arr[0]:
            # search on arr[:mid+1]
            loc = bisect.bisect_left(arr, target, 0, mid+1)
            if arr[loc] == target:
                return loc
            return -1
        else:
            # search on arr[mid+1:]
            loc = bisect.bisect_left(arr, target, mid+1, len(arr))
            if arr[loc] == target:
                return loc
            return -1

print(Solution().search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5))
print(Solution().search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 11))
print(Solution().search([1,1,1,1,1,2,1,1,1], 2))