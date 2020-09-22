# 面试题 16.20. T9键盘
#
# 20200810
# huao

from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        numToStr = ['', '', 'abc', 'def', 'ghi',
                    'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        matchedList = []
        for word in words:
            if len(word) != len(num):
                continue
            for i in range(len(word)):
                if not word[i] in numToStr[int(num[i])]:
                    break
            else:
                matchedList.append(word)
        return matchedList


sol = Solution()
print(sol.getValidT9Words(num="2", words=["a", "b", "c", "d"]))
