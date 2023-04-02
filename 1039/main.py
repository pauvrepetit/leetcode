from typing import List

# 唉，我也要感叹，我啥时候能写出这样的代码，动态规划还是得好好学习

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        min_scores = [[0xFFFFFFFF for _ in values] for _ in values]
        # min_scores[i][j] 表示，从i到j的这一段表示的多边形的最小分数
        for i in range(len(values) - 1):
            min_scores[i][i+1] = 0
        for i in range(len(values) - 2):
            min_scores[i][i+2] = values[i] * values[i+1] * values[i+2]
        
        for k in range(3, len(values)):
            for i in range(len(values) - k):
                j = i + k
                for l in range(i+1, j):
                    min_scores[i][j] = min(min_scores[i][j], min_scores[i][l] + min_scores[l][j] + values[i] * values[l] * values[j])
        return min_scores[0][len(values)-1]

print(Solution().minScoreTriangulation(values = [1,3,1,4,1,5]))
print(Solution().minScoreTriangulation(values = [3,7,4,5]))
print(Solution().minScoreTriangulation(values = [1,2,3]))
print(Solution().minScoreTriangulation(values = [3,5,2,5,2,6]))
print(Solution().minScoreTriangulation(values = [7,3,2,2,4,5,3]))
