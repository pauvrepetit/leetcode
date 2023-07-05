class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split()
        if len(ss) == 0:
            return ""
        res = ss[-1]
        for i in range(len(ss) - 1)[::-1]:
            res += " "
            res += ss[i]
        return res
