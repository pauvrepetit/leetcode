from typing import List

class Solution:
    def migRange(self, ranges: List[List[int]]) -> List[List[int]]:
        ranges.sort(key=lambda x : x[0])
        mig_ranges = []
        begin = ranges[0][0]
        end = ranges[0][1]
        for i in range(1, len(ranges)):
            if ranges[i][0] > end + 1:
                mig_ranges.append([begin, end])
                begin = ranges[i][0]
                end = ranges[i][1]
            else:
                end = max(end, ranges[i][1])
        mig_ranges.append([begin, end])
        return mig_ranges

    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = self.migRange(ranges)
        for begin, end in ranges:
            if left >= begin and right <= end:
                return True
        return False

print(Solution().isCovered([[1,2],[3,4],[5,6]], 2, 5))
