# 724. 寻找数组的中心索引
#
# 20200725
# huao
# 可以在O(n)的时间内完成的
# 先算总和
# 然后逐个的取list中的值，在此过程中就可以累计的计算出该值前面的和
# 然后用总和、该位置的值 就可以得到后面半部分的和
# 也就可以判断该位置是否满足中心索引的定义

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum += i

        localSum = 0
        index = 0
        for i in nums:
            if (sum - i) % 2 == 0 and (sum - i) // 2 == localSum:
                return index
            index += 1
            localSum += i
        return -1


sol = Solution()
print(sol.pivotIndex([1, 2, 3]))
