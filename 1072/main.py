from typing import List

#
# @lc app=leetcode.cn id=1072 lang=python3
#
# [1072] 按列翻转得到最大值等行数
#

# @lc code=start
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = dict()
        for i in matrix:
            s1 = ''
            s2 = ''
            for j in i:
                if j == 0:
                    s1 += '0'
                    s2 += '1'
                else:
                    s1 += '1'
                    s2 += '0'
            if s1 in count.keys():
                count[s1] += 1
            elif s2 in count.keys():
                count[s2] += 1
            else:
                count[s1] = 1
        return max(count.values())

# @lc code=end

print(Solution().maxEqualRowsAfterFlips([[0,1],[1,1]]))
