# 131. 分割回文串
#
# 20210730
# huao
# 就硬递归

from typing import List


class Solution:
    def check(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        res = []
        if self.check(s):
            res = [[s]]
        for i in range(1, len(s)):
            ss = s[:i]
            if self.check(ss):
                sub_part = self.partition(s[i:])
                for j in range(len(sub_part)):
                    sub_part[j].insert(0, ss)
                res += sub_part
        return res


print(Solution().partition("aa"))
