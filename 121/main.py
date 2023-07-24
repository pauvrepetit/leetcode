#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = [0 for _ in prices]
        max_val[-1] = prices[-1]
        for i in range(len(prices)-1)[::-1]:
            max_val[i] = max(max_val[i+1], prices[i])
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, max_val[i] - prices[i])
        return profit

# @lc code=end

print(Solution().maxProfit([1,2,11,4,7]))
