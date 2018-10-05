class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_len = len(J)
        num = 0
        for i in range(j_len):
            num += S.count(J[i])
        return num
