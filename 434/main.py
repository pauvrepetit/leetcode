# 434. 字符串中的单词数
#
# 20200810
# huao

class Solution:
    def countSegments(self, s: str) -> int:
        wordList = s.split(' ')
        count = 0
        for word in wordList:
            if word != '':
                count += 1
        return count
