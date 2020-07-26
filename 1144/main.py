# 1144. 递减元素使数组呈锯齿状
#
# 20200726
# huao
# 有两种调整方法，调奇数项/调偶数项
# 对于偶数项，需要单独考虑第一项
# 对于二者，都需要考虑最后一项

from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        numsLen = len(nums)
        count = 0
        for i in range(numsLen)[0::2]:
            if i == 0 and nums[0] >= nums[1]:
                count += (nums[0] - nums[1] + 1)
                continue
            elif i == numsLen // 2 * 2 and numsLen % 2 == 1 and nums[i] >= nums[i - 1]:
                count += (nums[i] - nums[i - 1] + 1)
                continue
            elif i != numsLen // 2 * 2 and i != 0 and (nums[i] >= nums[i - 1] or nums[i] >= nums[i + 1]):
                count += (nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
                continue

        minCount = count
        count = 0
        for i in range(numsLen)[1::2]:
            if numsLen % 2 == 0 and i == numsLen - 1 and nums[i] >= nums[i - 1]:
                count += (nums[i] - nums[i - 1] + 1)
                continue
            elif i != numsLen - 1 and (nums[i] >= nums[i - 1] or nums[i] >= nums[i + 1]):
                count += (nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
                continue
        return min(count, minCount)


sol = Solution()
print(sol.movesToMakeZigzag([7, 4, 8, 9, 7, 7, 5]))
