# 151. 翻转字符串里的单词
#
# 20200809
# huao
# python大法好

class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.strip(' ').split(' ')[::-1]
        s = ""
        for word in wordList:
            if word == '':
                continue
            s += (word + " ")
        return s[:len(s)-1]


sol = Solution()
print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords("  hello    world!  "))
