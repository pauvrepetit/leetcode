# 1567. 乘积为正数的最长子数组长度
# 周赛No.204
# 
# 20200905
# huao

from typing import List


def count(num):
    c = 0
    left = len(num)
    right = 0
    for i in range(len(num)):
        if num[i] < 0:
            c += 1
            left = min(left, i)
            right = max(right, i)
    return c, left, right


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        i = 0
        numList = []
        for j in range(len(nums)):
            if nums[j] == 0:
                if i != j:
                    numList.append(nums[i:j])
                i = j + 1
        if nums[i:] != []:
            numList.append(nums[i:])

        maxLen = 0
        for num in numList:
            c, left, right = count(num)
            if c % 2 == 0:
                maxLen = max(maxLen, len(num))
            else:
                maxLen = max(maxLen, len(num)-left-1, right)
        return maxLen


print(Solution().getMaxLen(nums=[1, -2, -3, 4]))
print(Solution().getMaxLen(nums=[0, 1, -2, -3, -4]))
print(Solution().getMaxLen(nums=[-1, -2, -3, 0, 1]))
print(Solution().getMaxLen(nums=[-1, 2]))
print(Solution().getMaxLen(nums=[1, 2, 3, 5, -6, 4, 0, 10]))
