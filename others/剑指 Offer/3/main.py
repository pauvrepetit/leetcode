# 剑指 Offer 03. 数组中重复的数字
#
# 20200725
# huao
# 这也是个简单题

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        count = [0 for i in range(len(nums))]
        for i in nums:
            if count[i] >= 1:
                return i
            else:
                count[i] += 1
        return -1
