# 324. 摆动排序 II
#
# 20200811
# huao
# 结果是O(n)的时间复杂度 或者 O(1)的额外空间复杂度 都没有做到...

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sortedNum = sorted(nums)
        length = len(nums)
        minPart = sortedNum[:(length+1)//2][::-1]
        maxPart = sortedNum[(length+1)//2:][::-1]
        for i in range(length):
            if i % 2 == 0:
                nums[i] = minPart[i // 2]
            else:
                nums[i] = maxPart[i // 2]
