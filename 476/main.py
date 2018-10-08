class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        numbin = list(bin(num)[2:])
        for i in range(len(numbin)):
            if numbin[i] == '1':
                numbin[i] = '0'
            else:
                numbin[i] = '1'
        numbin = "".join(numbin)
        return int(numbin, 2)

