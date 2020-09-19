# 57. 插入区间
#
# 20200919
# huao

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        outIntervals = []
        i = 0
        length = len(intervals)
        while i < length:
            if newInterval == []:
                outIntervals += intervals[i:]
                break
            interval = intervals[i]
            a, b = interval
            c, d = newInterval
            if b <= c:
                outIntervals.append(interval)
                i += 1
                continue
            if a <= c <= b <= d:
                outIntervals.append(interval)
                newInterval = [b, d]
                i += 1
                continue
            if a <= c <= d <= b:
                outIntervals.append(interval)
                outIntervals += intervals[i+1:]
                i += 1
                break
            if c <= a <= b <= d:
                outIntervals.append([c, b])
                newInterval = [b, d]
                i += 1
                continue
            if c <= a <= d <= b:
                outIntervals.append([c, b])
                outIntervals += intervals[i+1:]
                i += 1
                break
            if c <= d <= a <= b:
                outIntervals.append([c, d])
                outIntervals.append(interval)
                outIntervals += intervals[i+1:]
                i += 1
                break
        else:
            outIntervals.append(newInterval)
        i = 0
        while i < len(outIntervals)-1:
            a, b = outIntervals[i]
            c, d = outIntervals[i+1]
            if b == c:
                outIntervals.pop(i)
                outIntervals[i][0] = a
            else:
                i += 1
        return outIntervals


print(Solution().insert(intervals=[[1, 2], [3, 5], [
      6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
