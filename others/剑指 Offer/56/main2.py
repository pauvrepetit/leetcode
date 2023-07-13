from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0 for _ in range(32)]
        for num in nums:
            n = 0
            while num != 0:
                if num & 1 == 1:
                    count[n] += 1
                n += 1
                num >>= 1
        res = 0
        n = 0
        for c in count:
            c %= 3
            res += (c << n)
            n += 1
        return res
