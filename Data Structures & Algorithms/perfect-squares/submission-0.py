class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)

        for t in range(1, n+1):
            val=float("inf")
            for s in range(1, int(t**0.5)+1):
                sq = s*s
                val = min(val, 1+dp[t-sq])
            dp[t]=val
        
        return dp[-1]
