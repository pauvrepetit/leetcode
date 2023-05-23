from typing import List
#
# @lc app=leetcode.cn id=1090 lang=python3
#
# [1090] 受标签影响的最大值
#

# @lc code=start
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        vls = [[values[i], labels[i]] for i in range(len(values))]
        vls.sort(reverse=True)
        count = 0
        num_counted = 0
        label_count = [0 for i in range(20001)]
        for i in range(len(values)):
            if label_count[vls[i][1]] < useLimit:
                count += vls[i][0]
                num_counted += 1
                label_count[vls[i][1]] += 1
                if num_counted == numWanted:
                    break
        return count

# @lc code=end

