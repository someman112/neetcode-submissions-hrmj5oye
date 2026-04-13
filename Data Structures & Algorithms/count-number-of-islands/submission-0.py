class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or (i,j) in seen or grid[i][j] == "0":
                return 0
            
            seen.add((i,j))
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for x,y in dirs:
                dfs(i+x, j+y)
            
            return 1
        
        res= 0 

        for i in range(rows):
            for j in range(cols):
                
                if (i,j) not in seen:
                    res+=dfs(i,j)
        
        return res
        