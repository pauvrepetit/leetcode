from typing import List
import bisect
#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        begin = 0
        end = len(citations)
        mid = (begin + end) // 2
        while begin != mid:
            mid_value = citations[mid] - (len(citations) - mid)
            if mid_value > 0:
                end = mid
            elif mid_value == 0:
                return citations[mid]
            else:
                begin = mid
            mid = (begin + end) // 2
        if mid + 1 == len(citations):
            return min(len(citations) - mid, citations[mid])
        return max(min(len(citations) - mid, citations[mid]), min(len(citations) - mid - 1, citations[mid+1]))        
# @lc code=end

print(Solution().hIndex(citations = [1]))
print(Solution().hIndex([1,1,3]))

