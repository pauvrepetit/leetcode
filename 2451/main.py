from typing import List
#
# @lc app=leetcode.cn id=2451 lang=python3
#
# [2451] 差值数组不同的字符串
#

# @lc code=start
class Solution:
    def oddString(self, words: List[str]) -> str:
        subs = []
        for word in words:
            sub = []
            for i in range(1, len(word)):
                sub.append(ord(word[i]) - ord(word[i-1]))
            subs.append([sub, word])
        subs.sort()
        if subs[0][0] != subs[1][0]:
            return subs[0][1]
        return subs[-1][1]

# @lc code=end

