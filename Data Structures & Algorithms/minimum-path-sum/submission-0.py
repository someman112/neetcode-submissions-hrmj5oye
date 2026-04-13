class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[float("inf")]*n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if (i,j) == (0,0): continue 
                num1= dp[i-1][j] if i-1>=0 else float("inf")
                num2= dp[i][j-1] if j-1>=0 else float("inf")
                dp[i][j] = grid[i][j] + min(num1, num2)
        
        return dp[-1][-1]



        # @lru_cache(None)
        # def dfs(i,j):
        #     if not(0<=i<m and 0<=j<n): return float("inf")
        #     if (i,j) == (m-1,n-1): return grid[i][j]

        #     return grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
        
        # return dfs(0,0)