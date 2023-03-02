from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        min_path = [0 for i in range(n+1)]
        for i in range(n)[::-1]:
            for j in range(i+1):
                min_path[j] = triangle[i][j] + min(min_path[j], min_path[j+1])
        return min_path[0]

print(Solution().minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
print(Solution().minimumTotal(triangle = [[-10]]))
print(Solution().minimumTotal(triangle = [[-1],[-2,-3]]))
