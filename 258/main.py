# add-digits
# 各位相加


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        listnum = list(str(num))
        for i in range(len(listnum)):
            listnum[i] = int(listnum[i])
        sumnum = 0
        for n in listnum:
            sumnum += n
        if sumnum < 10:
            return sumnum
        else:
            return Solution.addDigits(self, sumnum)
