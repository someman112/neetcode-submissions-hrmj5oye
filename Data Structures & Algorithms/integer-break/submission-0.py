class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0] * (n+1)
        dp[1]=1

        for i in range(2, n+1):
            val = 0
            for j in range(1, i):
                val = max(val, j* max(i-j, dp[i-j]))
            dp[i]=val
        
        return dp[-1]
        