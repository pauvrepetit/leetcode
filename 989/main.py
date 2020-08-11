# 989. 数组形式的整数加法
#
# 20200811
# huao

from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = A[::-1]
        for i in range(len(A)):
            sum = A[i] + K
            K = sum // 10
            A[i] = sum % 10
            if K == 0:
                break
        else:
            KList = list(str(K))[::-1]
            for i in range(len(KList)):
                KList[i] = int(KList[i])
            A = A + KList
        return A[::-1]


sol = Solution()
print(sol.addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1))
