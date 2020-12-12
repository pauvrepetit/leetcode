# 5609. 统计一致字符串的数目
from typing import List

class Solution:
    def check(self, allowed: str, word: str) -> bool:
        count = 0
        for c in allowed:
            count += word.count(c)
        return count == len(word)

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if self.check(allowed, word):
                count += 1
        return count

