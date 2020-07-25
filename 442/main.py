# 442. 数组中重复的数据
#
# 20200725
# huao
# 这个题在O(n)的时间内完成是很简单的
# 但是要在O(n)的时间内不使用额外的内存空间实现，似乎不好办啊

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = [0 for i in range(len(nums))]
        for i in nums:
            count[i - 1] += 1
        numsTwice = []
        for i in range(len(count)):
            if count[i] == 2:
                numsTwice.append(i + 1)
        return numsTwice
