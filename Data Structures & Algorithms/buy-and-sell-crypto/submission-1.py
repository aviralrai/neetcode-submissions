class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        while l < len(prices):
            for r in range(l,len(prices)):
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
            l += 1
        return max_profit