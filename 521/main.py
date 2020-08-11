# 521. 最长特殊序列 Ⅰ
#
# 20200811
# huao

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))
