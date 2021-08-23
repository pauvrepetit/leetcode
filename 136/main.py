# 136. 只出现一次的数字
#
# 20210730
# huao
# emmm... 我是真不会写线性时间复杂度的算法
# 我好蠢呀
# 哈哈哈哈哈，我看到了位运算的tag，忽然就开窍了

from typing import List


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         for num in nums:
#             if nums.count(num) == 1:
#                 return num


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for n in nums:
            num ^= n
        return num
