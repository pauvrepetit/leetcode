# 976. 三角形的最大周长
#
# 20200728
# huao
# 就判断最大的三个数字能不能构成三角形，如果不能的话，说明最大的那个数字肯定是不能包含在其中的
# 那么就去掉最大值，在剩下的数字中找最大的三个数

from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=1)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0


sol = Solution()
print(sol.largestPerimeter([2, 1, 2]))
print(sol.largestPerimeter([1, 2, 1]))
print(sol.largestPerimeter([3, 2, 3, 4]))
print(sol.largestPerimeter([3, 6, 2, 3]))
