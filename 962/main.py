# 962. 最大宽度坡
#
# 20200802
# huao
# i < j 且 nums[i] <= nums[j] 则为坡 width = j - i
# 这个在时间上存在一些问题...
# 终究还是过了 就是很慢

from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        length = len(A)
        if length == 0:
            return 0

        B = [(A[i], i) for i in range(length)]
        B.sort(key=lambda x: x[0])

        nums = [B[i][1] for i in range(length)]
        optNums = [(nums[length-1], length-1)]
        i = 0
        for i in range(length-1)[::-1]:
            if nums[i] > optNums[0][0]:
                optNums.insert(0, (nums[i], i))

        maxWidth = 0
        i = 0
        j = 0
        for i in range(length-1):
            while optNums[j][1] <= i:
                j += 1
            maxWidth = max(maxWidth, optNums[j][0] - nums[i])
        return maxWidth


sol = Solution()
print(sol.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
