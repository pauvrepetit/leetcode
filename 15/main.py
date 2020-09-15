# 15. 三数之和
#
# 20200915
# huao

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tuples = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            begin = i+1
            end = len(nums)-1
            while begin < end and nums[end] >= 0:
                if nums[begin] + nums[end] + nums[i] == 0:
                    tuples.append([nums[i], nums[begin], nums[end]])
                    beginNum = nums[begin]
                    while begin < end and nums[begin] == beginNum:
                        begin += 1
                    endNum = nums[end]
                    while end > begin and nums[end] == endNum:
                        end -= 1
                elif nums[begin] + nums[end] + nums[i] < 0:
                    beginNum = nums[begin]
                    while begin < end and nums[begin] == beginNum:
                        begin += 1
                else:
                    endNum = nums[end]
                    while end > begin and nums[end] == endNum:
                        end -= 1
        return tuples


print(Solution().threeSum(nums=[0, 0, 0]))
