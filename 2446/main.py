from typing import List
#
# @lc app=leetcode.cn id=2446 lang=python3
#
# [2446] 判断两个事件是否存在冲突
#

# @lc code=start
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        a, b = event1
        c, d = event2
        return not (b < c or d < a)

# @lc code=end

