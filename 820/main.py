# 820. 单词的压缩编码
#
# 20200811
# huao

from typing import List
from functools import cmp_to_key


def cmp(x: str, y: str) -> int:
    return len(y) - len(x)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=cmp_to_key(cmp))
        maxWords = []
        for word in words:
            for maxWord in maxWords:
                if maxWord.endswith(word):
                    break
            else:
                maxWords.append(word)
        length = 0
        for word in maxWords:
            length += (len(word) + 1)
        return length


sol = Solution()
print(sol.minimumLengthEncoding(["time", "time", "time", "time"]))
