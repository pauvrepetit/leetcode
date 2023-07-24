#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from typing import List
from typing import Optional

# @lc code=start
class Solution:
    def comp(self, s: str, begin: int, wordDict: List[str], breaked: List[int]) -> bool:
        if breaked[begin] == 1:
            return True
        if breaked[begin] == 0:
            return False
        for word in wordDict:
            if s[begin:].startswith(word):
                if self.comp(s, begin + len(word), wordDict, breaked):
                    breaked[begin+len(word)] = 1
                    return True
        breaked[begin] = 0
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        breaked = [-1 for _ in range(len(s)+1)]
        breaked[-1] = 1
        # 记录s[i:]是否能够break
        # -1 未知
        # 0 不能
        # 1 能
        return self.comp(s, 0, wordDict, breaked)

# @lc code=end

