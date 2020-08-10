# 面试题 16.21. 交换和
#
# 20200810
# huao

from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        array1.sort()
        array2.sort()
        sum1 = 0
        for num in array1:
            sum1 += num
        sum2 = 0
        for num in array2:
            sum2 += num

        if (sum2 - sum1) % 2 != 0:
            return []
        sub = (sum2 - sum1) // 2
        i = 0
        j = 0
        while i < len(array1) and j < len(array2):
            if array2[j] - array1[i] == sub:
                return [array1[i], array2[j]]
            elif array2[j] - array1[i] > sub:
                i += 1
            else:
                j += 1
        return []
