class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        num = []
        for i in range(left, right + 1):
            stri = str(i)
            leni = len(stri)
            for j in range(leni):
                if stri[j] == '0' or i % int(stri[j]) != 0:
                    num.append(i)
                    break
        renum = []
        for i in range(left, right + 1):
            if i not in num:
                renum.append(i)
        return renum
