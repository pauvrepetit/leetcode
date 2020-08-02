# 628. 三个数的最大乘积
#
# 20200802
# huao
# 排序自然是很优雅的
# 但是这个题的话 排序还是比较慢的 因为没有必要
# 我们直接遍历一遍 其实就可以得到所有5个我们需要的元素
# 最大值 次大值 次次大值 最小值 次小值

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # length = len(nums)
        # return max(nums[0] * nums[1] * nums[length-1], nums[length-1] * nums[length-2] * nums[length-3])
        length = len(nums)
        i = 0
        exceptList = []
        maxNum1 = -2000
        maxNum2 = -2000
        maxNum3 = -2000
        minNum1 = 2000
        minNum2 = 2000
        for num in nums:
            if num >= maxNum1:
                maxNum3 = maxNum2
                maxNum2 = maxNum1
                maxNum1 = num
            elif num >= maxNum2:
                maxNum3 = maxNum2
                maxNum2 = num
            elif num >= maxNum3:
                maxNum3 = num

            if num <= minNum1:
                minNum2 = minNum1
                minNum1 = num
            elif num <= minNum2:
                minNum2 = num
        return max(maxNum1*maxNum2*maxNum3, maxNum1*minNum1*minNum2)
