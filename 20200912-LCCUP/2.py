# LCP 18. 早餐组合
# LeetCode CUP 2020 Fall
#
# 20200912
# huao

from typing import List
import bisect


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        length = len(drinks)
        count = 0
        for s in staple:
            count += bisect.bisect_right(drinks, x - s)
            count %= 1000000007
        return count


print(Solution().breakfastNumber(staple=[10, 20, 5], drinks=[5, 5, 2], x=15))
print(Solution().breakfastNumber(staple=[2, 1, 1], drinks=[8, 9, 5, 1], x=9))
