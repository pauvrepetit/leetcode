from typing import List

#
# @lc app=leetcode.cn id=1330 lang=python3
#
# [1330] 翻转子数组得到最大的数组值
#
# 写一下大致思路吧
# 通过分析我们发现，翻转一个子数组，对数组值的影响只发生在子数组的起始和终止位置，
# 准确的说，翻转a_i到a_j的子数组，影响只取决于a_(i-1)\a_i\a_j\a_(j+1)这四个数，更准确的说，是这四个数中大小位于中间的两个值
# 通过验证我们发现，i-1和i的两个数一组，j和j+1的两个数一组，如果这两组有重叠（或者包含）关系，
# 那么当前已经是最大值，当二者没有重叠关系时，可以通过调整取到更大的值
# 所以对于这种情况，我们遍历一遍数组即可，找到两两数对中，较小值的最大值，和较大值的最小值，
# 也就是四个数中，在可调整的情况下，的中间两个值
# 判断这两个值的大小，可以确定，他是否有重叠关系
# 特殊情况，含边界的调整，我们单独考虑

# @lc code=start
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        value = 0
        max_value = -0xFFFFFFF
        min_value = 0xFFFFFFF
        for i in range(len(nums) - 1):
            value += abs(nums[i+1] - nums[i])
            max_value = max(max_value, min(nums[i], nums[i+1]))
            min_value = min(min_value, max(nums[i], nums[i+1]))
        if max_value > min_value:
            res_value = value + 2 * (max_value - min_value)
        else:
            res_value = value

        for i in range(1, len(nums) - 1):
            if abs(nums[i+1] - nums[i]) < abs(nums[i+1] - nums[0]):
                res_value = max(res_value, value - abs(nums[i+1] - nums[i]) + abs(nums[i+1] - nums[0]))
            if abs(nums[i+1] - nums[i]) < abs(nums[-1] - nums[i]):
                res_value = max(res_value, value - abs(nums[i+1] - nums[i]) + abs(nums[-1] - nums[i]))
        return res_value

# @lc code=end
