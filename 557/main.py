# reverse-words-in-a-string-iii
# 反转字符串中的单词III


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split(" ")
        relist = []
        for i in range(len(slist)):
            relist.append(slist[i][::-1])
        return " ".join(relist)
