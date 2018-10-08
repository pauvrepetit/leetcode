# excel-sheet-column-number
# excel表列序号


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        slen = len(s)
        slist = list(s)
        for i in range(slen):
            num += (ord(slist[i]) - 64) * pow(26, slen - i - 1)
        return num
