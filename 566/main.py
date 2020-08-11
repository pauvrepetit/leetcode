# 566. 重塑矩阵
#
# 20200811
# huao
# 这用numpy就是偷懒
# 当然 肯定没有自己手写快就是了

from typing import List
import numpy as np


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        npNums = np.array(nums)
        if npNums.size != r * c:
            return nums
        npNums = npNums.reshape(r, c)
        return npNums.tolist()
