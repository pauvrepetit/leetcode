from typing import List
#
# @lc app=leetcode.cn id=2559 lang=python3
#
# [2559] 统计范围内的元音字符串数
#

# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        sums = [1 if word[0] in "aeiou" and word[-1] in "aeiou" else 0 for word in words]
        sums.insert(0, 0)
        for i in range(1, n+1):
            sums[i] = sums[i] + sums[i-1]
        return [sums[j+1] - sums[i] for i, j in queries]

# @lc code=end

