# 1288. 删除被覆盖区间
#
# 20200911
# huao

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)
        i = 0
        while i < len(intervals):
            for j in range(len(intervals)):
                if i != j and intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    intervals.pop(i)
                    break
            else:
                i += 1
        return len(intervals)


print(Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
