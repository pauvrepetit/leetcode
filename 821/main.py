# shortest-distance-to-a-character
# 字符的最短距离


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        shortlen = []
        for i in range(len(S)):
            len0 = len(S)
            for j in range(i, -1, -1):
                if S[j] == C:
                    len0 = min(len0, i - j)
                    break
            for j in range(i, len(S), 1):
                if S[j] == C:
                    len0 = min(len0, j - i)
                    break
            shortlen.append(len0)
        return shortlen
