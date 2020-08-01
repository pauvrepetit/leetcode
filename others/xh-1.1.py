# xh-1.1. 求数组中每个数第一次出现的位置
#
# 20200801
# huao

from typing import List


class Solution:
    def find_left_repeat_num(self, nums: List[int]) -> List[int]:
        numShow = {}
        resList = []
        i = 0
        for num in nums:
            if num in numShow.keys():
                resList.append(numShow[num])
            else:
                numShow[num] = i
                resList.append(-1)
            i += 1
        return resList


sol = Solution()
print(sol.find_left_repeat_num([1, 3, 1, 2, 1]))
