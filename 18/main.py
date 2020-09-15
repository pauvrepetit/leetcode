# 18. 四数之和
#
# 20200915
# huao

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        fourNums = []
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue

                begin = j+1
                end = len(nums)-1
                while begin < end:
                    if nums[i] + nums[j] + nums[begin] + nums[end] == target:
                        fourNums.append(
                            [nums[i], nums[j], nums[begin], nums[end]])
                        beginNum = nums[begin]
                        while begin < end and nums[begin] == beginNum:
                            begin += 1
                        endNum = nums[end]
                        while begin < end and nums[end] == endNum:
                            end -= 1
                    elif nums[i] + nums[j] + nums[begin] + nums[end] < target:
                        beginNum = nums[begin]
                        while begin < end and nums[begin] == beginNum:
                            begin += 1
                    else:
                        endNum = nums[end]
                        while begin < end and nums[end] == endNum:
                            end -= 1
        return fourNums


print(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
