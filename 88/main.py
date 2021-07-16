# 88. 合并两个有序数组
#
# 20210716
# huao

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums = nums1[:]
        i, j, loc = 0, 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums[loc] = nums1[i]
                i += 1
            else:
                nums[loc] = nums2[j]
                j += 1
            loc += 1
        if i == m:
            while j < n:
                nums[loc] = nums2[j]
                loc += 1
                j += 1
        else:
            while i < m:
                nums[loc] = nums1[i]
                loc += 1
                i += 1
        for i in range(m + n):
            nums1[i] = nums[i]


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
