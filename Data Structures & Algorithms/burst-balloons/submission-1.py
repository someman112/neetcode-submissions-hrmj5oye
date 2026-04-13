class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]


        for ln in range(n):

            for i in range(n-ln):
                j = i+ln

                for k in range(i, j+1):

                    left_sub = dp[i][k-1] if (k-1)>=i else 0
                    right_sub = dp[k+1][j] if (k+1)<=j else 0 

                    left_mult = nums[i-1] if i-1>=0 else 1
                    right_mult = nums[j+1] if j+1<n else 1 

                    res = left_sub + (left_mult * nums[k] * right_mult) + right_sub
                    dp[i][j] = res if res > dp[i][j] else dp[i][j] 
        
        return dp[0][n-1]
        