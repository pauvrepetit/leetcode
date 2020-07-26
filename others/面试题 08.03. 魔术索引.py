# 面试题 08.03. 魔术索引
#
# 20200726
# huao
# 扫一遍就好

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1
