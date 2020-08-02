# 890. 查找和替换模式
#
# 20200802
# huao
# 逐个的check

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matchWords = []
        for word in words:
            if self.checkWord(word, pattern):
                matchWords.append(word)
        return matchWords

    def checkWord(self, word: str, pattern: str) -> bool:
        posMap = {}
        negMap = {}
        length = len(word)
        for i in range(length):
            if word[i] in posMap.keys():
                if pattern[i] != posMap[word[i]]:
                    return False
            else:
                posMap[word[i]] = pattern[i]

            if pattern[i] in negMap.keys():
                if word[i] != negMap[pattern[i]]:
                    return False
            else:
                negMap[pattern[i]] = word[i]
        return True
