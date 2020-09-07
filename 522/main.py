# 522. 最长特殊序列 II
#
# 20200907
# huao

from typing import List


def subStr(s: str, lstr: str) -> bool:
    i = 0
    j = 0
    while i < len(s):
        if j == len(lstr):
            return False
        if s[i] == lstr[j]:
            i += 1
            j += 1
        else:
            j += 1
    return True


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        lenStr = [[] for i in range(11)]
        for str in strs:
            lenStr[len(str)].append(str)
        longerStr = []
        for ss in lenStr[::-1]:
            i = 0
            while i < len(ss):
                s = ss[i]
                for lstr in longerStr:
                    if subStr(s, lstr):
                        while s in ss:
                            ss.remove(s)
                        break
                else:
                    i += 1
            if len(ss) == 0:
                continue
            if len(ss) == 1:
                return len(ss[0])
            for s in ss:
                if ss.count(s) == 1:
                    return len(s)
                longerStr.append(s)
        return -1


print(Solution().findLUSlength(
    ["abcabc", "abcabc", "abcabc", "abc", "abc", "aab"]))
print(Solution().findLUSlength(["aaa", "aaa", "aa"]))
print(Solution().findLUSlength(["aabbcc", "aabbcc", "cb", "abc"]))
