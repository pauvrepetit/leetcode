#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from typing import List

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counts = [-1 for _ in range(amount+1)]
        counts[0] = 0
        for i in range(1, len(counts)):
            if i in coins:
                counts[i] = 1
            else:
                count = i+1
                for j in coins:
                    if i > j and counts[i-j] != -1:
                        count = min(count, counts[i-j]+1)
                if count != i+1:
                    counts[i] = count
        return counts[-1]

# @lc code=end

