class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        # 记录以当前点结尾的最大收益/当前点的最大收益
        max_profit = [0 for _ in range(len(prices))]
        now_profit = [0 for _ in range(len(prices))]
        now_profit[1] = prices[1] - prices[0]
        if now_profit[1] > 0:
            max_profit[1] = now_profit[1]
        for i in range(2, len(prices)):
            now_profit[i] = max(now_profit[i-1] + prices[i] - prices[i-1], prices[i] - prices[i-1])
            max_profit[i] = max(max_profit[i-1], now_profit[i])
        return max_profit[-1]
