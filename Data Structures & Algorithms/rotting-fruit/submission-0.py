from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        num_fresh = 0
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == 2:
                    q.append((i,j, 0))

                elif grid[i][j] == 1:
                    num_fresh+=1
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        mins = 0

        while q:
            i,j,curr_time = q.popleft()

            mins = max(mins, curr_time)

            for x,y in dirs:
                ix = i+x
                jy = j+y

                if 0<=ix<rows and 0<=jy<cols and grid[ix][jy] == 1:
                    grid[ix][jy] = 2
                    q.append((ix, jy, curr_time+1))
                    num_fresh-=1
        
        if num_fresh:
            return -1
        
        return mins