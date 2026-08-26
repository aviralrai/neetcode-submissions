class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m_p = 0
        profit = 0
        for i in range(1,len(prices)):
            profit+= prices[i] - prices[i-1]
            if profit < 0:
                profit = 0
            m_p = max(profit,m_p)
        return m_p
        