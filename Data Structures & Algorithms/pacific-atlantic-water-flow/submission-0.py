class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, visited, prevHeight):
            if (i < 0 or j < 0 or i>=rows or j>=cols or (i,j) in visited or heights[i][j] < prevHeight):
                return
            
            visited.add((i,j))

            dirs = [(0,1), (1,0), (0,-1), (-1,0)]
            for x,y in dirs:
                dfs(i+x, j+y, visited, heights[i][j])
            
        
        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i,cols-1, atl, heights[i][cols-1])
        
        for i in range(cols):
            dfs(0, i, pac, heights[0][i])
            dfs(rows-1, i, atl, heights[rows-1][i])
        
        return list(pac.intersection(atl))
        