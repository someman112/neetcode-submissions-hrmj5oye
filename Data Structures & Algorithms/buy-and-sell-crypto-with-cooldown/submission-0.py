class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -prices[0]
        rest = 0
        sell = 0


        for i in range(1, len(prices)):
            buy  = max(buy, rest - prices[i])
            rest = max(rest, sell)
            sell = buy + prices[i]

        return max(rest, sell)

        