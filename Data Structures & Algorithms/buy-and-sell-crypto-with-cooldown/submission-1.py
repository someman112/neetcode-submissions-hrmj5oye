class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_hold = -prices[0]
        cool_down = 0 
        sell = 0


        for i in range(1, len(prices)):
            buy_hold = max(buy_hold, cool_down - prices[i])
            cool_down = max(cool_down, sell)
            sell = buy_hold + prices[i]
        
        return max(cool_down, sell)



        