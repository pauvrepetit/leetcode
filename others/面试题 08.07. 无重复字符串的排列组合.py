# 面试题 08.07. 无重复字符串的排列组合
#
# 20200810
# huao

from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        if S == "":
            return []
        strList = []
        for c in S:
            newS = S.replace(c, '')
            subList = self.permutation(newS)
            if subList == []:
                strList.append(c)
            for subS in subList:
                strList.append(c + subS)
        return strList


sol = Solution()
print(sol.permutation("qwe"))
