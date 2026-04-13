from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            i,j = q.popleft()

            for x,y in dirs:
                ix = i+x
                jy = j+y
                if 0<=ix<rows and 0<=jy<cols and grid[ix][jy] == 2147483647:
                    grid[ix][jy] = grid[i][j]+1
                    q.append((ix, jy))
        
        






        