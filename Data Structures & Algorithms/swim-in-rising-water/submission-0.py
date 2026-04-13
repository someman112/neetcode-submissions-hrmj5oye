class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        res = 0
        hp = [(grid[0][0], 0, 0)]
        visited = set()

        while hp:
            dist, r, c = heapq.heappop(hp)
            res = max(res, dist)

            if (r,c) == (rows-1, cols-1):
                return res

            for dx, dy in dirs:
                x = r + dx
                y = c + dy

                if (0<=x<rows and 0<=y<cols and (x,y) not in visited):
                    heapq.heappush(hp, (grid[x][y],x,y))
                    visited.add((x,y))