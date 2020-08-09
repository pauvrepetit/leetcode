# 944. 删列造序
#
# 20200809
# huao
# 慢啊

from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A) == 0:
            return 0
        B = []
        for i in range(len(A[0])):
            s = ""
            for j in range(len(A)):
                s += A[j][i]
            B.append(s)
        count = 0
        for b in B:
            count += self.check(b)
        return count

    def check(self, s: str) -> int:
        for i in range(1, len(s)):
            if s[i-1] > s[i]:
                return 1
        return 0


sol = Solution()
print(sol.minDeletionSize(["cba", "daf", "ghi"]))
