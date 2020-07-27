# 1296. 划分数组为连续数字的集合
#
# 20200727
# huao
# 这个时间用的很有点长...
# 当然，细节上可以改进的，毕竟很多库函数在特定情况下有更好更快的实现方法

from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        while len(nums) > 0:
            delNumBegin = nums[0]
            for i in range(k):
                try:
                    nums.remove(delNumBegin + i)
                except ValueError:
                    return False
        return True


sol = Solution()
print(sol.isPossibleDivide([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
