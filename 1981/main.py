from typing import List

#
# @lc app=leetcode.cn id=1981 lang=python3
#
# [1981] 最小化目标值与所选元素的差
#
# 这种DP我还真没写过

# @lc code=start
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        maxc = 1
        for i in mat:
            maxc += max(i)

        f = [[False for _ in range(maxc)] for _ in range(70)]
        m = len(mat)
        n = len(mat[0])
        b = False
        for i in range(n):
            f[0][mat[0][i]] = True
        for j in range(1, m):
            b = False
            for i in range(maxc):
                if b:
                    continue
                if not f[j-1][i]:
                    continue
                if i > target:
                    b = True
                for k in range(n):
                    if i+mat[j][k] < maxc:
                        f[j][i+mat[j][k]] = f[j-1][i]
        t = 100000
        for i in range(maxc):
            if f[m-1][i]:
                t = min(t, abs(target - i))
        return t
# @lc code=end

print(Solution().minimizeTheDifference([[1],[2],[3]], 100))
print(Solution().minimizeTheDifference([[65],[45],[45],[69],[55],[60],[29],[25],[16],[5],[62],[16],[29],[19],[34],[2],[24],[32],[66],[62],[60],[46],[42],[37],[51],[4],[41],[4],[66],[20],[9],[4],[66],[6],[56],[10],[51],[44],[7],[8],[5],[44],[28],[7],[10],[7],[24],[62],[19],[14],[45],[68],[9],[14],[51],[28],[8],[57],[59],[6],[54],[8],[19],[16],[63],[45],[33],[15],[33],[67]], 800))
