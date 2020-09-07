# 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
#
# 20200907
# huao

from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for num in nums:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)
        return odd + even
