# 1455. 检查单词是否为句中其他单词的前缀
#
# 20200728
# huao
# 找前缀 startswith而已

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i + 1
        return -1
