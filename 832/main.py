class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        lenlist = len(A)
        B = []
        # flip
        for i in range(lenlist):
            B.append(A[i].reverse())
        # invert
        for i in range(lenlist):
            for j in range(lenlist):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1

        return A
