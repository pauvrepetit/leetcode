# 1190. 反转每对括号间的子串
#
# 20200810
# huao
# 正则表达式真是处理字符串的好东西

import re


class Solution:
    def reverseParentheses(self, s: str) -> str:
        pattern = "\([^\(\)]*\)"
        words = re.findall(pattern, s)
        while words != []:
            for word in words:
                s = s.replace(word, word[len(word)-2:0:-1])
            words = re.findall(pattern, s)
        return s


sol = Solution()
print(sol.reverseParentheses("(u(love)i)"))
