# 80. 删除有序数组中的重复项 II
#
# 20210719
# huao

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if nums[0] == nums[1]:
            fast = 2
            slow = 1
        else:
            fast = 1
            slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                if fast != len(nums) - 1 and nums[fast] == nums[fast + 1]:
                    slow += 1
                    nums[slow] = nums[fast]
                    slow += 1
                    nums[slow] = nums[fast]
                else:
                    slow += 1
                    nums[slow] = nums[fast]
        return slow + 1
