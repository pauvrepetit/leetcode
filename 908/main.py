# smallest-range-i
# 最小差值I


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxnum = max(A)
        minnum = min(A)
        if (maxnum - minnum) >= K * 2:
            return maxnum - minnum - K * 2
        else:
            return 0
