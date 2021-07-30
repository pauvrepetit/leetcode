# 201. 数字范围按位与
#
# 20210730
# huao

from math import log2

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        left_log = int(log2(left))
        right_log = int(log2(right))
        if left_log != right_log:
            return 0
        return 2 ** left_log + self.rangeBitwiseAnd(left - 2 ** left_log, right - 2 ** right_log)
