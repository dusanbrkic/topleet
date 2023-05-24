class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buyPrice = prices[0]
        for i in range(len(prices)):
            buyPrice = min(prices[i], buyPrice)
            profit = max(profit, prices[i] - buyPrice)
        return profit