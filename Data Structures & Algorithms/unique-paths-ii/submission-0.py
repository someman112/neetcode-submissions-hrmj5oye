class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]: return 0
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1

        for i in range(m):
            for j in range(n):
                num1= 0 if j-1<0 or obstacleGrid[i][j-1]==1 else dp[i][j-1]
                num2= 0 if i-1<0 or obstacleGrid[i-1][j]==1 else dp[i-1][j]
                dp[i][j]+=num1+num2
        
        return dp[-1][-1]

        # @lru_cache(None)
        # def dfs(i,j):
        #     if not (0<=i<m and 0<=j<n) or obstacleGrid[i][j] == 1: return 0
        #     if i==m-1 and j==n-1: return 1

        #     return dfs(i+1, j) + dfs(i,j+1)
        
        # return dfs(0,0)