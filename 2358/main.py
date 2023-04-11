from math import sqrt
from typing import List
#
# @lc app=leetcode.cn id=2358 lang=python3
#
# [2358] 分组的最大数量
#

# @lc code=start
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return int((sqrt(8 * len(grades) + 1) - 1) / 2)
# @lc code=end

# 和数据都没什么关系的，脑筋急转弯一般的题目
