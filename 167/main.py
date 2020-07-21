# 167. 两数之和 II - 输入有序数组
#
# 20200720
# huao
#
# 就是个简单的二分查找

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            num1 = numbers[i]
            num2 = self.binary_search(
                numbers, target - num1, i + 1, len(numbers))
            if num2 != -1:
                return [i + 1, num2 + 1]
        return [0, 0]

    def binary_search(self, numbers: List[int], target: int, begin: int, end: int) -> int:
        mid = (int)((begin + end) / 2)
        if mid == begin:
            if numbers[mid] == target:
                return mid
            else:
                return -1
        elif numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            return self.binary_search(numbers, target, mid, end)
        elif numbers[mid] > target:
            return self.binary_search(numbers, target, begin, mid)
        else:
            return -1


sol = Solution()
print(sol.twoSum([1, 2, 3, 4, 5], 8))
