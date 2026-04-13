class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n=len(heights), len(heights[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        hp = [(0,0,0)]
        visited = set()

        while hp:
            diff, i, j = heapq.heappop(hp)
            if (i,j) in visited: continue 
            
            visited.add((i,j))
            if (i,j) == (m-1, n-1): return diff

            for x,y in dirs:
                nx,ny = i+x, j+y

                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                    n_diff = max(diff,abs(heights[i][j]-heights[nx][ny]))
                    heapq.heappush(hp, (n_diff,nx,ny))
