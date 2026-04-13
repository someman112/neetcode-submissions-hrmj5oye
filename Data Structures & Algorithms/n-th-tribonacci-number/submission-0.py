class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[0, 1, 1]

        if n < 3: return dp[n]

        i=3
        while i <=n:
            num = dp[-1] + dp[-2] + dp[-3]
            dp.append(num)
            i+=1
        
        return dp[-1]