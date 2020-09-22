# 剑指 Offer 51. 数组中的逆序对
#
# 20200909
# huao

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.sol(nums, 0, len(nums))

    def sol(self, nums: List[int], begin: int, end: int) -> int:
        if begin == end:
            return 0
        elif begin+1 == end:
            return 0
        elif begin+2 == end:
            if nums[begin] > nums[begin+1]:
                temp = nums[begin]
                nums[begin] = nums[begin+1]
                nums[begin+1] = temp
                return 1
            else:
                return 0
        mid = (begin + end) // 2
        left = self.sol(nums, begin, mid)
        right = self.sol(nums, mid, end)
        count = left + right

        leftNums = nums[begin:mid] + [0xFFFFFFFFFFFF]
        rightNums = nums[mid:end] + [0xFFFFFFFFFFFF]
        loc = begin
        i = 0
        j = 0
        while i < (mid-begin) or j < (end-mid):
            while j < (end-mid) and leftNums[i] > rightNums[j]:
                nums[loc] = rightNums[j]
                loc += 1
                j += 1
            if i < (mid-begin):
                count += j
                nums[loc] = leftNums[i]
                loc += 1
                i += 1
        return count


print(Solution().reversePairs([4, 5, 6, 7]))
