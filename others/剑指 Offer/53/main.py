# 剑指 Offer 53 - I. 在排序数组中查找数字 I
#
# 20200730
# huao
# 二分查找
# 在C++的STL中有直接的函数可以实现这里的操作

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = self.searchLeft(nums, target, 0, len(nums))
        right = self.searchRight(nums, target, 0, len(nums))
        if left == -1:
            return 0
        else:
            return right - left + 1

    def searchLeft(self, nums: List[int], target: int, begin: int, end: int) -> List[int]:
        if begin == end:
            return -1
        elif begin + 1 == end and nums[begin] == target:
            return begin
        elif begin + 1 == end:
            return -1
        elif begin + 2 == end:
            if nums[begin] == target:
                return begin
            elif nums[begin + 1] == target:
                return begin + 1
            else:
                return -1

        mid = (begin + end) // 2
        if nums[mid] < target:
            return self.searchLeft(nums, target, mid, end)
        else:
            return self.searchLeft(nums, target, begin, mid + 1)

    def searchRight(self, nums: List[int], target: int, begin: int, end: int) -> List[int]:
        if begin == end:
            return -1
        elif begin + 1 == end and nums[begin] == target:
            return begin
        elif begin + 1 == end:
            return -1
        elif begin + 2 == end:
            if nums[begin + 1] == target:
                return begin + 1
            elif nums[begin] == target:
                return begin
            else:
                return -1

        mid = (begin + end) // 2
        if nums[mid] <= target:
            return self.searchRight(nums, target, mid, end)
        else:
            return self.searchRight(nums, target, begin, mid + 1)
