class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        diff = 0
        l, r = 0 , 1

        while r < N:
            diff = max(diff, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            
            r+=1

        return  diff
        
        