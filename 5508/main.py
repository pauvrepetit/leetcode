# 5508. 数的平方等于两数乘积的方法数
# 周赛No.205
#
# 20200906
# huao

from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1dic = {}
        nums2dic = {}
        for i in nums1:
            if i in nums1dic.keys():
                continue
            nums1dic[i] = nums1.count(i)
        for i in nums2:
            if i in nums2dic.keys():
                continue
            nums2dic[i] = nums2.count(i)

        count = 0
        for i in range(len(nums1)):
            for j in nums2dic.keys():
                if nums1[i] * nums1[i] % j != 0:
                    continue
                numk = nums1[i] * nums1[i] // j
                if numk > j and numk in nums2dic.keys():
                    count += nums2dic[numk] * nums2dic[j]
                elif numk == j:
                    count += (nums2dic[numk] * (nums2dic[numk]-1)) // 2

        for i in range(len(nums2)):
            for j in nums1dic.keys():
                if nums2[i] * nums2[i] % j != 0:
                    continue
                numk = nums2[i] * nums2[i] // j
                if numk > j and numk in nums1dic.keys():
                    count += nums1dic[numk] * nums1dic[j]
                elif numk == j:
                    count += (nums1dic[numk] * (nums1dic[numk]-1)) // 2
        return count


print(Solution().numTriplets(nums1=[7, 4], nums2=[5, 2, 8, 9]))
print(Solution().numTriplets(nums1=[1, 1], nums2=[1, 1, 1]))
print(Solution().numTriplets(nums1=[7, 7, 8, 3], nums2=[1, 2, 9, 7]))
print(Solution().numTriplets(
    nums1=[4, 7, 9, 11, 23], nums2=[3, 5, 1024, 12, 18]))
print(Solution().numTriplets([4, 1, 4, 1, 12], [3, 2, 5, 4]))
