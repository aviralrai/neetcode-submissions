class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_profit = 0
        for r in range(len(prices)):
            profit = prices[r] - min_buy
            if profit > max_profit:
                max_profit = profit
            if prices[r] < min_buy:
                min_buy = prices[r]
        return max_profit