# 62. 不同路径
# 组合数，杨辉三角

yanghui = [[0 for i in range(202)] for j in range(202)]


def comb(n, k):
    if yanghui[n][k] == 0:
        yanghui[n][k] = (comb(n-1, k-1) + comb(n-1, k))
    return yanghui[n][k]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        for i in range(202):
            yanghui[i][0] = 1
            yanghui[i][i] = 1
        return comb(m+n-2, min(m, n)-1)