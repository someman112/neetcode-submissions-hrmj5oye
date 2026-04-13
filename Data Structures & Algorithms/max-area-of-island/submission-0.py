class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        def dfs(i,j):
            if i < 0 or j < 0 or i>=rows or j>=cols or grid[i][j] == 0:
                return 0 
            
            grid[i][j] = 0 
            area = 1
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]

            for x, y in dirs:
                area+=dfs(i+x, j+y)
            
            return area
        
        ans = 0

        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j]:
                    ans = max(ans, dfs(i,j))
        
        return ans
        