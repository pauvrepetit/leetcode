#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from typing import List

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        count = dict()
        for c in "abcdefghijklmnopqrstuvwxyz":
            count[c] = 0
        for c in p:
            count[c] -= 1
        for i in range(len(p)):
            count[s[i]] += 1
        res = []
        for val in count.values():
            if val != 0:
                break
        else:
            res.append(0)
        for i in range(len(s) - len(p)):
            count[s[i]] -= 1
            count[s[i+len(p)]] += 1
            for val in count.values():
                if val != 0:
                    break
            else:
                res.append(i+1)
        return res

# @lc code=end

print(Solution().findAnagrams("aa", "aa"))
