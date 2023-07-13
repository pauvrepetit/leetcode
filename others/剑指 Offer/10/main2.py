class Solution:
    def numWays(self, n: int) -> int:
        ways = [0 for _ in range(105)]
        ways[1] = 1
        # ways[i] = ways[i-1] + ways[i-2]
        for i in range(2, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]
