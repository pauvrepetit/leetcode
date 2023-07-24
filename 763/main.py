#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from typing import List

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s == "":
            return []
        exists = set(s[0])
        prev_index = 1
        while True:
            index = 1
            for c in exists:
                index = max(len(s) - s[::-1].find(c), index)
            if prev_index == index:
                break
            prev_index = index
            exists = set(s[:prev_index])
        return [prev_index] + self.partitionLabels(s[prev_index:])

# @lc code=end

