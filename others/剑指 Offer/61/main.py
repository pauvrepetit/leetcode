from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        min_val = 20
        max_val = -1
        non_zero_vals = []
        for num in nums:
            if num == 0:
                continue
            min_val = min(min_val, num)
            max_val = max(max_val, num)
            non_zero_vals.append(num)
        return len(set(non_zero_vals)) == len(non_zero_vals) and max_val - min_val <= 4
