# 26. 删除排序数组中的重复项
#
# 20200722
# huao
# 扫一遍，也必须要扫一遍吧
# 很简单的一个题

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[count]:
                count += 1
                nums[count] = nums[i]
        return count + 1