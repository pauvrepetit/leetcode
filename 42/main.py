# 42. 接雨水
#
# 20200727
# huao
# emmm...
# 虽然测试过了，但是似乎这个做法很慢呢


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        uniqueHeight = sorted(list(set(height)))
        heightLen = len(height)
        count = 0
        lastH = 0
        for h in uniqueHeight:
            minIndex = 0
            for i in range(0, heightLen):
                if height[i] >= h:
                    minIndex = i
                    break
            maxIndex = 0
            for i in range(minIndex, heightLen)[::-1]:
                if height[i] >= h:
                    maxIndex = i
                    break
            if minIndex == maxIndex:
                continue
            else:
                for i in range(minIndex, maxIndex):
                    if height[i] < h:
                        count += (h - lastH)
            lastH = h
        return count


sol = Solution()
print(sol.trap([4, 2, 3]))
