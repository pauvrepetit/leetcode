# binary-number-with-alternating-bits
# 交替位二进制数


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nbin = bin(n)
        if '11' not in nbin and '00' not in nbin:
            return True
        else:
            return False
