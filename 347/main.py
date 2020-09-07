# 347. 前 K 个高频元素
#
# 20200907
# huao

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            if num in numCount.keys():
                numCount[num] += 1
            else:
                numCount[num] = 1
        numCountList = []
        for key in numCount.keys():
            numCountList.append([key, numCount[key]])
        numCountList.sort(key=lambda x: x[1])
        topList = []
        for i in range(len(numCountList))[::-1][:k]:
            topList.append(numCountList[i][0])
        return topList


print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(Solution().topKFrequent(nums=[1], k=1))
