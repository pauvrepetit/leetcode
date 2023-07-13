from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum = num ^ xor_sum
        count = 0
        while xor_sum & 1 == 0:
            count += 1
            xor_sum >>= 1
        xor_sum = 1 << count
        left_xor_sum = 0
        right_xor_sum = 0
        for num in nums:
            if num & xor_sum == 0:
                left_xor_sum = num ^ left_xor_sum
            else:
                right_xor_sum = num ^ right_xor_sum
        return [left_xor_sum, right_xor_sum]
