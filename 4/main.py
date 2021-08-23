# 4. 寻找两个正序数组的中位数
#
# 20210729
# huao
# 这个题其实写个merge就没意思了，可惜我不会做

from typing import List


class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        nums = []
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        for k in range(i, len1):
            nums.append(nums1[k])
        for k in range(j, len2):
            nums.append(nums2[k])
        return nums

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.merge(nums1, nums2)
        lens = len(nums)
        if lens % 2 == 1:
            return nums[lens // 2]
        else:
            return (nums[lens // 2 - 1] + nums[lens // 2]) / 2


print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([1, 3], [2, 4]))
