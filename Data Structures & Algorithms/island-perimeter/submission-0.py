class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        m,n = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(i,j):
            if (i,j) in visited:
                return 0
            
            visited.add((i,j))
            ans=0
            for dx,dy in dirs:
                x,y = i+dx, j+dy

                if x < 0 or x>=m or y < 0 or y>=n or grid[x][y]==0:
                    ans+=1
                else:
                    ans+=dfs(x, y)
            
            return ans
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i,j)