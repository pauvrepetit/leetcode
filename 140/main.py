# 140. 单词拆分 II
#
# 20200802
# huao
# 很暴力的解法...
# 存在一些很长的测试样例
# 但是这些样例似乎都是不能够完成拆分的
# 所有我们在最开始做一个大致判断 根据字典中出现过的字母 和 输入串中的字母
# 而那些大样例在这一阶段 估计都被筛选掉了
# 事实上，这种大样例本身就是很难于解决的
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sLen = len(s)
        sChar = []
        for word in wordDict:
            for c in word:
                if c not in sChar:
                    sChar.append(c)
        for c in s:
            if c not in sChar:
                return []
        strList = []
        for i in range(1, sLen+1):
            if s[:i] in wordDict:
                if i == sLen:
                    strList.append(s[:i])
                else:
                    subStrList = self.wordBreak(s[i:], wordDict)
                    for subStr in subStrList:
                        strList.append(s[:i] + " " + subStr)
        return strList


sol = Solution()
print(sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
