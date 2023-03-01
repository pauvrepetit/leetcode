from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # 简单分析就知道，这个范围只有两种可能
        # 要么左边是0，要么右边是n
        # 所以就是贪心
        n = len(colors)
        left_color = colors[0]
        right_color = colors[-1]
        if left_color != right_color:
            return n - 1
        else:
            maxD = 0
            for left in range(n):
                if colors[left] != left_color:
                    maxD = max(maxD, n - 1 - left)
            for right in range(n)[::-1]:
                if colors[right] != right_color:
                    maxD = max(maxD, right)
            return maxD

print(Solution().maxDistance(colors = [1,1,1,6,1,1,1]))
print(Solution().maxDistance(colors = [1,8,3,8,3]))
print(Solution().maxDistance(colors = [0,1]))
