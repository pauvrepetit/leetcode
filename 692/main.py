# 692. 前K个高频单词
#
# 20200811
# huao
# 统计 排序
# 其实是有点浪费的

from typing import List
from functools import cmp_to_key


def cmp(x, y) -> int:
    if x[0] == y[0]:
        if y[1] < x[1]:
            return 1
        elif y[1] == x[1]:
            return 0
        else:
            return -1
    else:
        if y[0] > x[0]:
            return 1
        else:
            return -1


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = []
        while words != []:
            word = words[0]
            num = words.count(word)
            wordCount.append([num, word])
            for i in range(num):
                words.remove(word)
        wordCount.sort(key=cmp_to_key(cmp))
        topKWord = []
        for i in range(k):
            topKWord.append(wordCount[i][1])
        return topKWord


sol = Solution()
print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
