# 30. 串联所有单词的子串
#
# 20200722
# huao
# 这个肯定是不能从单词列表入手的，单词列表可以产生的排列数是阶乘级的，复杂度太高
# 所有我们从输入字符串入手，扫一遍就ok了
# 因为单词列表中，每个单词的长度都是相同的，且已知，单词个数也是已知的
# 如果找到一个单词，那么判断从该位置开始的那么多个字母，按照单词长度分割以后和单词列表是不是一样就ok了
# 所有整体上，其实就是对输入字符串扫描了一遍

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        wordLen = len(words[0])
        subStringLen = wordLen * len(words)
        subStrList = []
        for i in range(len(s) - subStringLen + 1):
            if s[i:i+wordLen] in words:
                if self.checkString(s[i:i+subStringLen], words) == 1:
                    subStrList.append(i)
        return subStrList

    def checkString(self, s: str, words: List[str]) -> int:
        wordLen = len(words[0])
        wordsInStr = []
        for i in range(len(words)):
            wordsInStr.append(s[i*wordLen:i*wordLen+wordLen])
        if sorted(wordsInStr) == sorted(words):
            return 1
        else:
            return 0


sol = Solution()
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
