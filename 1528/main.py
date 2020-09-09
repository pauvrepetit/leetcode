# 1528. 重新排列字符串
#
# 20200909
# huao

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ss = [0 for i in range(len(s))]
        for i in range(len(s)):
            ss[indices[i]] = s[i]
        return ''.join(c for c in ss)
    # 我傻了 用排序来做
    # def restoreString(self, s: str, indices: List[int]) -> str:
    #     slist = []
    #     for i in range(len(s)):
    #         slist.append([s[i], indices[i]])
    #     slist.sort(key=lambda x: x[1])
    #     s = ""
    #     for c, _ in slist:
    #         s += c
    #     return s


print(Solution().restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
