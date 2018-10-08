# array-partition-i
# 数组拆分


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortnums = sorted(nums)
        sum = 0
        for i in range(0, len(nums), 2):
            sum += sortnums[i]
        return sum
