# 60. 第k个排列
#
# 20200905
# huao

A = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.cal(n, k-1)

    def cal(self, n: int, k: int) -> str:
        if n == 1:
            return "1"
        num = k // A[n-2] + 1
        leftNum = self.cal(n-1, k % A[n-2])
        resNum = str(num)
        for i in range(len(leftNum)):
            if int(leftNum[i]) >= num:
                resNum += str(int(leftNum[i])+1)
            else:
                resNum += leftNum[i]
        return resNum


print(Solution().getPermutation(4, 9))
