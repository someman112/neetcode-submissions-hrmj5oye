class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices)-1):
            res+= prices[i+1] - prices[i] if prices[i+1] > prices[i] else 0
        
        return res
        