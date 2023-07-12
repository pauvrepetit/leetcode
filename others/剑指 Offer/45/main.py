from typing import List

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        length = 0
        str_nums = []
        for num in nums:
            str_nums.append(str(num))
            length = max(length, len(str(num)))
        str_nums.sort(key=lambda x : [x + x + x[0] * (length - len(x))])
        res = ""
        for s in str_nums:
            res += s
        return res
