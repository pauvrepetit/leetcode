from typing import List
#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        index = 0
        for i in range(len(citations)):
            index = max(index, min(i+1, citations[i]))
        return index
# @lc code=end

print(Solution().hIndex([1,3,1]))