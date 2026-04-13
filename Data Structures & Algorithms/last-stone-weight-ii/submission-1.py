class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ= sum(stones)
        target= summ // 2
        dp = [False] * (target+1)
        dp[0]=True

        for stone_weight in stones:
            for capacity in range(target, stone_weight-1, -1):
                dp[capacity] = dp[capacity] or dp[capacity-stone_weight]

        for capacity in range(target,-1,-1):
            if dp[capacity]: return abs(capacity-(summ-capacity))
                

        

        