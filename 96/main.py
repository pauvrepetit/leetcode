# 96. 不同的二叉搜索树
#
# 20200727
# huao
# 算是个简单的动态规划吧

from typing import List


class Solution:
    def numTrees(self, n: int) -> int:
        nums = [0 for i in range(n + 1)]
        return self.calNumTrees(n, nums)

    def calNumTrees(self, n: int, nums: List[int]) -> int:
        if n == 0:
            nums[n] = 1
            return 1
        if nums[n] != 0:
            return nums[n]
        for i in range(n // 2):
            nums[n] += self.calNumTrees(i, nums) * \
                self.calNumTrees(n - i - 1, nums) * 2
        if n % 2 != 0:
            nums[n] += self.calNumTrees(n // 2, nums) * \
                self.calNumTrees(n // 2, nums)
        return nums[n]


sol = Solution()
print(sol.numTrees(3))
