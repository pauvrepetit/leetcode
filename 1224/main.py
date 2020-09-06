# 1224. 最大相等频率
#
# 20200906
# huao

from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        numCount = {}
        for num in nums:
            if num in numCount.keys():
                numCount[num] += 1
            else:
                numCount[num] = 1

        for i in range(len(nums))[::-1]:
            values = numCount.values()
            valuesList = list(values)
            values = list(set(values))
            if len(values) == 1 and (values[0] == 1 or valuesList.count(values[0]) == 1):
                return i+1
            if len(values) != 2:
                numCount[nums[i]] -= 1
                if numCount[nums[i]] == 0:
                    numCount.pop(nums[i])
            else:
                if values[0] + 1 == values[1] and valuesList.count(values[1]) == 1:
                    return i+1
                if values[0] == values[1] + 1 and valuesList.count(values[0]) == 1:
                    return i+1
                if values[1] == 1 and valuesList.count(values[1]) == 1:
                    return i+1
                if values[0] == 1 and valuesList.count(values[0]) == 1:
                    return i+1
                numCount[nums[i]] -= 1
                if numCount[nums[i]] == 0:
                    numCount.pop(nums[i])
        return 0


print(Solution().maxEqualFreq(nums=[2, 2, 1, 1, 5, 3, 3, 5]))
print(Solution().maxEqualFreq(nums=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]))
print(Solution().maxEqualFreq(nums=[1, 1, 1, 2, 2, 2]))
print(Solution().maxEqualFreq(nums=[10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]))
print(Solution().maxEqualFreq([1, 2, 3, 1, 2, 3, 4, 4, 4, 4, 1, 2, 3, 5, 6]))
print(Solution().maxEqualFreq([1, 1, 2, 3, 3, 4, 4, 5, 30, 31, 38, 48, 99, 13, 57, 29, 59, 85, 36, 95, 94, 19, 55, 36, 17, 49, 11, 61, 23, 89, 49, 36, 5, 86, 39, 26, 28, 12, 45, 34, 45, 19, 34, 92, 47, 74, 75, 97, 19,
                               14, 33, 98, 46, 66, 98, 3, 93, 95, 30, 24, 77, 20, 64, 32, 45, 91, 41, 28, 95, 7, 36, 2, 92, 42, 90, 96, 53, 57, 26, 70, 15, 54, 51, 28, 46, 82, 66, 68, 89, 43, 90, 36, 44, 51, 40, 29, 98, 16, 34, 90, 11, 100, 2]))
