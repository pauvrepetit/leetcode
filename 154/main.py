# 154. 寻找旋转排序数组中的最小值 II
# 剑指 Offer 11. 旋转数组的最小数字
#
# 20200722
# huao
# 这个其实还真是不好做呀
# O(n)的算法自然是非常简单的，直接扫一遍就完了
# 但是这个list本身是由两段排好序的list组合而成的，这个条件实在是不太好用上啊

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        for i in range(len(nums)):
            minNum = min(minNum, nums[i])
        return minNum
        

sol = Solution()
print(sol.findMin([1,3,3]))
