class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount

        for c in coins:

            for i in range(1, amount+1):
                if i>=c:
                    dp[i]+= dp[i-c]
            
        
        return dp[-1]
        