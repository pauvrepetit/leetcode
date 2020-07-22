# 27. 移除元素
#
# 20200722
# huao
# 用list最后的元素来填充被移除的val，从而避免所有剩余元素的移动
# 注意终止时count和last的关系

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        count = 0
        while count <= last:
            if nums[count] == val:
                nums[count] = nums[last]
                last -= 1
            else:
                count += 1
        return count