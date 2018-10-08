# transpose-matrix
# 转置矩阵


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        newrow = []
        newlist = []
        for c in range(col):
            newrow = []
            for r in range(row):
                newrow.append(A[r][c])
            newlist.append(newrow)
        return newlist
